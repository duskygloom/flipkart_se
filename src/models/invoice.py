from rich.box import SQUARE
from rich.panel import Panel
from rich.table import Table

from utils.time import *
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
        console.print()
        title_panel = Panel(f"[bold]Invoice[/bold]", SQUARE, expand=False)
        console.print(title_panel, justify="center")
        console.print()
        console.print(f"[bold]Seller:[/bold] {self.order.seller.name}")
        seller_address = self.order.seller.address
        console.print(f"[bold]Seller address:[/bold] {seller_address}")
        console.print()
        console.print(f"[bold]Order time:[/bold] {get_current_strftime()}")
        console.print(f"[bold]Buyer:[/bold] {self.order.buyer.name}")
        buyer_address = self.order.buyer.address
        console.print(f"[bold]Buyer address:[/bold] {buyer_address}")
        console.print()
        console.print(self.order.get_products_table())
        console.print()


__all__ = [
    "Invoice"
]
