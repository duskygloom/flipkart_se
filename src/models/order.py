from datetime import datetime

from rich.box import SQUARE
from rich.table import Table

from utils.styles import *
from utils.currency import *

from models.user import *
from models.product import *


class Order:
    buyer: User
    bought_time: str
    products: list[Product]

    def __init__(self, buyer: User, bought_time: str, products: list[Product]):
        self.buyer = buyer
        self.bought_time = bought_time
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
        styles = get_styles()
        table = Table("ID", "Name", "Seller", "Price", "Discount", "Total", box=SQUARE, show_lines=True, header_style=styles['app_title'])
        for product in self.products:
            table.add_row(
                str(product.product_id),
                product.name,
                product.seller.name if product.seller is not None else "-",
                get_currency_string(product.price),
                get_currency_string(product.discount),
                get_currency_string(product.price - product.discount)
            )
        total_amount_str = get_currency_string(self.get_total_amount())
        table.add_row(f"[{styles['app_title']}]Total amount[/]", "", "", "", "", total_amount_str)
        return table


__all__ = [
    "Order"
]
