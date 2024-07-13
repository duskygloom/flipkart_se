from rich.box import SQUARE
from rich.panel import Panel
from rich.table import Table

from utils.time import *
from utils.styles import *
from utils.console import *

from models.order import Order


class Invoice:
    order: Order

    def __init__(self, order: Order) -> None:
        self.order = order

    def get_invoice_table(self) -> Table:
        table = Table()
        table.add_row("Seller", self.order.seller.name)
        table.add_row("Seller address", self.order.seller.address)
        table.add_row()
        table.add_row("Buyer", self.order.buyer.name)
        table.add_row("Buyer address", self.order.buyer.address)
        table.add_row()
        table.add_row("Order time", self.order.bought_time)
        return table

    def print(self):
        styles = get_styles()
        console.print(f"[{styles['app_title']}]Time:[/] {self.order.bought_time}")
        console.print(f"[{styles['app_title']}]Buyer:[/] {self.order.buyer.name}")
        buyer_address = self.order.buyer.address
        console.print(f"[{styles['app_title']}]Buyer address:[/] {buyer_address}")
        console.print()
        console.print(self.order.get_products_table())


__all__ = [
    "Invoice"
]
