'''
Contains classes and functions related to fetching and
storing products from and into databases.
'''

from models.product import Product


class Store:
    @staticmethod
    def search(query: str) -> list[Product]:
        products = []
        sql_query = "select * from products where keywords like *%s"
        return products


__all__ = [
    "Store"
]
