'''
Contains classes and functions related to fetching and
storing products from and into databases.
'''

from typing import Generator

from mariadb import ProgrammingError

from rich.box import SQUARE
from rich.table import Table
from rich.prompt import Prompt

from utils.sql import *
from utils.time import *
from utils.config import *
from utils.styles import *
from utils.console import *
from utils.currency import *

from models.user import *
from models.order import *
from models.product import *
from models.invoice import *
from models.account_manager import *


def get_result_table(products: list[Product]) -> Table:
    styles = get_styles()
    table = Table("ID", "Name", "Description", "Price", "Offer", box=SQUARE, show_lines=True, header_style=styles['app_title'])
    for product in products:
        table.add_row(str(product.product_id), product.name, product.description, get_currency_string(product.price), get_currency_string(product.price-product.discount))
    return table


def product_available(product_id: int) -> bool:
    sql = SQL.get_default()
    sql.execute(f"select buyer_name from transactions where product_id = {product_id} and isnull(bought_time)")
    return bool(len(sql.fetchone()))


class Store:
    sql: SQL
    config: config_t

    def __init__(self):
        self.sql = SQL.get_default()
        self.config = get_config()

    def search(self, query: str) -> Table:
        query = query.lower()
        self.sql.execute(f"select * from products natural join transactions where isnull(bought_time) and (keywords like '%,{query},%' or keywords like '%,{query}' or keywords like '{query},%' or keywords like '{query}')")
        results = self.sql.fetchall()
        products = [Product.from_tuple(result) for result in results]
        return get_result_table(products)

    def add_to_cart(self, product_id: int) -> bool:
        # fetch the buyer
        buyer = AccountManager.logged_user()
        if not buyer:
            console.print("Log into your account to buy.")
            return False
        # check if available
        if not product_available(product_id):
            console.print_warning(f"Product {product_id} has already been sold.")
            return False
        # update transactions
        self.sql.execute(f"update transactions set buyer_name = '{self.config['current_user']}' where product_id = {product_id}", commit=True)
        return True

    def get_cart(self, user: User) -> Table:
        styles = get_styles()
        if user.name != self.config["current_user"]:
            console.print_error(f"[{styles['highlight']}]{user.name}[/] has logged out.")
            return None
        # get data before purchase
        self.sql.execute(f"select product_id, name, keywords, description, price, discount, seller_name from products natural join transactions where buyer_name = '{user.name}' and isnull(bought_time)")
        products = []
        for row in self.sql.fetchall():
            product = Product.from_tuple(row[:6])
            product.seller = User.from_name(row[6])
            products.append(product)
        # create table
        table = Table("ID", "Name", "Price", "Seller", box=SQUARE, show_lines=True, header_style=styles['app_title'])
        for product in products:
            seller_name = "-"
            if product.seller:
                seller_name = product.seller.name
            price = get_currency_string(product.price - product.discount)
            table.add_row(str(product.product_id), product.name, str(price), seller_name)
        return table
    
    def buy(self, user: User) -> Invoice:
        styles = get_styles()
        if user.name != self.config["current_user"]:
            console.print_error(f"[{styles['highlight']}]{user.name}[/] has logged out.")
            return None
        # get data before purchase
        self.sql.execute(f"select product_id, name, description, keywords, price, discount, seller_name from products natural join transactions where buyer_name = '{user.name}' and isnull(bought_time)")
        products = []
        for row in self.sql.fetchall():
            product = Product.from_tuple(row[:6]) 
            product.seller = User.from_name(row[6])
            products.append(product)
        # proceed with purchase
        order = Order(user, get_current_strftime(), products)
        if self.sql.execute(f"update transactions set bought_time = '{order.bought_time}', bought_price = {order.get_total_amount()} where buyer_name = '{user.name}' and isnull(bought_time)", commit=True):
            return Invoice(order)
        return None
    
    def get_bought_history(self, user: User) -> Table:
        styles = get_styles()
        if user.name != self.config["current_user"]:
            console.print_error(f"[{styles['highlight']}]{user.name}[/] has logged out.")
            return None
        # get data
        self.sql.execute(f"select product_id, name, seller_name, bought_time, bought_price from products natural join transactions where buyer_name = '{user.name}' and not isnull(bought_time)")
        # create table
        table = Table("ID", "Name", "Seller", "Time", "Price", box=SQUARE, show_lines=True, header_style=styles['app_title'])
        for row in self.sql.fetchall():
            bought_time = get_strftime(row[3]) if row[3] else "-"
            bought_price = get_currency_string(row[4]) if row[4] else "-"
            table.add_row(str(row[0]), row[1], row[2], bought_time, bought_price)
        return table
    
    def get_sold_history(self, user: User) -> Table:
        styles = get_styles()
        if user.name != self.config["current_user"]:
            console.print_error(f"[{styles['highlight']}]{user.name}[/] has logged out.")
            return None
        # get data
        self.sql.execute(f"select product_id, name, sold_time, buyer_name, bought_time, bought_price from products natural join transactions where seller_name = '{user.name}'")
        # create table
        table = Table("ID", "Name", "Sold time", "Buyer", "Bought time", "Price", box=SQUARE, show_lines=True, header_style=styles['app_title'])
        for row in self.sql.fetchall():
            bought_time = get_strftime(row[4]) if row[4] else "-"
            sold_price = get_currency_string(row[5]) if row[5] else "-"
            table.add_row(str(row[0]), row[1], get_strftime(row[2]), row[3] or "-", bought_time, sold_price)
        return table

    def sell(self) -> bool:
        '''
        Description
        -----------
        Prompts, sells and returns status.
        '''
         # fetch the buyer
        seller = AccountManager.logged_user()
        if not seller:
            console.print("Log into your account to sell.")
            return None
        # prompt
        name = Prompt.ask("Product name")
        keywords = Prompt.ask("Keywords (comma separated)")
        description = Prompt.ask("Description")
        price = Prompt.ask("Price")
        discount = Prompt.ask("Discount")
        # product id does not matter now, it will be assigned by database
        product = Product(-1, name, keywords, description, float(price), float(discount))
        # add product to products table
        product_query = product.get_product_sell_query()
        if not self.sql.execute(product_query):
            console.print_error("Could not add product to database.")
            self.sql.rollback()
            return False
        if not self.sql.execute("select max(product_id) from products"):
            console.print_error("Could not fetch the latest product from table.")
            return False
        product.product_id = self.sql.fetchone()[0]
        # add product to transactions table
        transaction_query = product.get_product_transaction_query(seller)
        if not self.sql.execute(transaction_query):
            console.print_error("Could not add product to database.")
            self.sql.rollback()
            return False
        self.sql.commit()
        return True


__all__ = [
    "Store"
]
