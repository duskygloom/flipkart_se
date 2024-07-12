'''
Contains classes and functions related to fetching and
storing products from and into databases.
'''

from typing import Generator

from utils.sql import *
from utils.time import *
from utils.config import *
from utils.console import *

from models.user import *
from models.order import *
from models.product import *
from models.invoice import *

config = get_config()


class Store:
    sql: SQL

    def __init__(self):
        self.sql = SQL.get_default()

    def search(self, query: str) -> Generator[list[Product], None, None]:
        self.sql.execute(query)
        results = self.sql.fetchmany(config['result_per_page'])
        if len(results) > 0:
            yield [Product.from_tuple(result) for result in results]
        else:
            return

    def buy(self, product_id: int) -> Invoice:
        self.sql.execute(f"select price-discount from product where product_id = {product_id}")
        price_tuple = self.sql.fetchone()
        if (len(price_tuple) < 1):
            logger.error(f"Could not complete transaction for product {product_id}")
            return None
        price = price_tuple[0]
        self.sql.execute(f"update transactions set buyer_name = '{config['current_user']}', bought_time = '{get_current_strftime()}', bought_price = {price} where product_id = {product_id};")
        self.sql.commit()
        self.sql.execute(f"select username, address from accounts where username = '{config['current_user']}")
        buyer_tuple = self.sql.fetchone()
        self.sql.execute(f"select username, address from accounts natural join transactions where product_id = '{product_id}")
        seller_tuple = self.sql.fetchone()
        return Invoice(Order(Buyer.from_tuple(buyer_tuple), get_current_strftime(), Seller.from_tuple(seller_tuple)))

    def sell(self):
        ...


__all__ = [
    "Store"
]
