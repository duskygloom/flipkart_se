'''
Contains classes and functions related to fetching and
storing products from and into databases.
'''

from typing import Generator

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
    # panel_text = ""
    # styles = get_styles()
    # for product in products:
    #     panel_text += f"[{styles['app_title']}]ID[/]{11*' '}[{styles['app_body']}]{product.product_id}[/]\n"
    #     panel_text += f"[{styles['app_title']}]Name[/]{9*' '}[{styles['app_body']}]{product.name}[/]\n"
    #     panel_text += f"[{styles['app_title']}]Description[/]{2*' '}[{styles['app_body']}]{product.description}[/]\n"
    #     panel_text += f"[{styles['app_title']}]Price[/]{8*' '}[{styles['app_body']}]{get_currency_string(product.price)}[/]\n"
    #     panel_text += f"[{styles['app_title']}]Discount[/]{5*' '}[{styles['app_body']}]{get_currency_string(product.discount)}[/]\n"
    # panel_text = panel_text.rstrip()
    # return Panel(panel_text, box=SQUARE, title=f"[{styles['highlight']}]Results[/]")
    table = Table("ID", "Name", "Description", "Price", "Discount", caption="Results", box=SQUARE)
    for product in products:
        table.add_row(str(product.product_id), product.name, product.description, get_currency_string(product.price), get_currency_string(product.discount))
    return table

class Store:
    sql: SQL
    config = get_config()

    def __init__(self):
        self.sql = SQL.get_default()

    def search(self, query: str) -> Generator[Table | str, None, None]:
        self.sql.execute(f"select * from products natural join transactions where isnull(buyer_name) and (keywords like '%,{query},%' or keywords like '%,{query}' or keywords like '{query},%' or keywords like '{query}')")
        results = self.sql.fetchmany(self.config['result_per_page'])
        while len(results) > 0:
            products = [Product.from_tuple(result) for result in results]
            results = self.sql.fetchmany(self.config['result_per_page'])
            yield get_result_table(products) if len(products) > 0 else ""
        return

    def buy(self, product_id: int) -> Invoice:
        # fetch the buyer
        buyer = AccountManager.logged_user()
        if not buyer:
            console.print("Log into your account to buy.")
            return None
        # find the current price
        self.sql.execute(f"select price-discount from product where product_id = {product_id}")
        price_tuple = self.sql.fetchone()
        if len(price_tuple) < 1:
            console.print_error(f"Could not complete transaction for product {product_id}")
            return None
        price = price_tuple[0]
        # update transactions
        self.sql.execute(f"update transactions set buyer_name = '{self.config['current_user']}', bought_time = '{get_current_strftime()}', bought_price = {price} where product_id = {product_id}")
        # fetch the seller
        self.sql.execute(f"select username, address, contact from accounts natural join transactions where product_id = '{product_id}")
        seller = Seller.from_tuple(self.sql.fetchone())
        if not seller:
            console.print("Could not find the seller.")
            self.sql.rollback()
            return None
        self.sql.commit()
        return Invoice(Order(buyer, get_current_strftime(), seller))

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
