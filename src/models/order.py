from datetime import datetime

from rich.box import SQUARE
from rich.table import Table

from utils.currency import get_currency_string

from models.user import *
from models.product import *


class Order:
    buyer: Buyer
    bought_time: str
    seller: Seller
    products: list[Product]

    def __init__(self, buyer: Buyer, bought_time: str, seller: Seller, products: list[Product]):
        self.buyer = buyer
        self.bought_time = str
        self.seller = seller
        self.products = products

    def get_total_amount(self) -> float:
        '''
        Returns
        -------
        Cost of all the products in the order.
        '''
        total_amount = 0
        for product in self.products:
            total_amount += product.price - product.discount
        return total_amount

    def get_products_table(self) -> Table:
        table = Table(box=SQUARE, show_lines=True)
        table.add_column("Name")
        table.add_column("Price", justify="right")
        table.add_column("Discount", justify="right")
        table.add_column("Total", justify="right")
        for product in self.product_qty:
            qty = self.product_qty[product]
            table.add_row(
                product.name,
                get_currency_string(product.price),
                get_currency_string(product.discount),
                get_currency_string(product.get_total_amount())
            )
        total_amount_str = get_currency_string(self.get_total_amount())
        table.add_row("Total amount", "", "", "", "", total_amount_str, style="bold")
        return table


__all__ = [
    "Order"
]
