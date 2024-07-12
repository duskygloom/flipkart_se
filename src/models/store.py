'''
Contains classes and functions related to fetching and
storing products from and into databases.
'''

from typing import Generator

from rich.prompt import Prompt

from utils.sql import *
from utils.time import *
from utils.config import *
from utils.console import *

from models.user import *
from models.order import *
from models.product import *
from models.invoice import *
from models.account_manager import *

config = get_config()


class Store:
    sql: SQL

    def __init__(self):
        self.sql = SQL.get_default()

    def search(self, query: str) -> Generator[list[Product], None, None]:
        self.sql.execute(f"select * from products natural join transactions where buyer_name = NULL and (keywords like '{query}' or keywords like '{query},%' or keywords like '%,{query}' or keywords like '%, {query}' or keywords like '%,{query},%' or keyword like '%, {query},%')")
        results = self.sql.fetchmany(config['result_per_page'])
        console.print(results)
        if len(results) > 0:
            yield [Product.from_tuple(result) for result in results]
        else:
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
            logger.error(f"Could not complete transaction for product {product_id}")
            return None
        price = price_tuple[0]
        # update transactions
        self.sql.execute(f"update transactions set buyer_name = '{config['current_user']}', bought_time = '{get_current_strftime()}', bought_price = {price} where product_id = {product_id}",commit=True)
        # fetch the seller
        self.sql.execute(f"select username, address from accounts natural join transactions where product_id = '{product_id}")
        seller = Seller.from_tuple(self.sql.fetchone())
        if not seller:
            console.print("Could not find the seller.")
            return False
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
        product_query = product.get_product_sell_query(seller)
        if not self.sql.execute(product_query, commit=True):
            logger.error("Could not add product to database.")
            return False
        if not self.sql.execute("select max(product_id) from products"):
            logger.error("Could not fetch the latest product from table.")
            return False
        product.product_id = self.sql.fetchone()[0]
        # add product to transactions table
        transaction_query = product.get_product_transaction_query(seller)
        if not self.sql.execute(transaction_query, commit=True):
            logger.error("Could not add product to database.")
            return False
        return True


__all__ = [
    "Store"
]
