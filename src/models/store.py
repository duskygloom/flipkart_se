'''
Contains classes and functions related to fetching and
storing products from and into databases.
'''

from models.product import Product

class Store:
    @staticmethod
    def search(query: str) -> list[Product]:
        products = []
        # fetch from database
        return products

__all__ = [
    "Store"
]
