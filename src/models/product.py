from models.user import *

from utils.sql import *
from utils.time import *


class Product:
    product_id: int
    name: str
    keywords: list[str]
    description: str
    price: float
    discount: float
    seller: User

    def __init__(self, product_id: int, name: str, keywords: str, description: str, price: float, discount: float):
        self.product_id = product_id
        self.name = name
        self.keywords = [word.strip() for word in keywords.split(',')]
        self.description = description
        self.price = price
        self.discount = discount

    @staticmethod
    def from_tuple(row: tuple) -> "Product":
        if len(row) < 6:
            return None
        return Product(row[0], row[1], row[2], row[3], row[4], row[5])
    
    @staticmethod
    def from_id(product_id: int) -> "Product":
        sql = SQL.get_default()
        sql.execute(f"select * from products where product_id = {product_id}")
        return Product.from_tuple(sql.fetchone())
    
    def get_product_sell_query(self) -> str:
        '''
        Description
        -----------
        Returns the query to be ran in the products table
        when a new product is added by a seller.
        '''
        query = "insert into products (name, keywords, description, price, discount) values "
        query += f"('{self.name}', '{','.join(self.keywords)}', '{self.description}', {self.price}, {self.discount})"
        return query
    
    def get_product_transaction_query(self, seller: User) -> str:
        '''
        Description
        -----------
        Returns the query to be ran in the transactions table
        when a new product is added by a seller.
        '''
        query = "insert into transactions (product_id, seller_name, sold_time) values "
        query += f"('{self.product_id}', '{seller.name}', '{get_current_strftime()}')"
        return query


__all__ = [
    "Product"
]
