from rich.box import SQUARE
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

from models.order import Order
from models.product import Product


class Invoice:
    invoice_id: str
    order: Order
    product_qty: dict[Product, int]
    shipment_charge: float

    def __init__(self, invoice_id: str, order: Order) -> None:
        self.invoice_id = invoice_id
        self.order = order

    def get_invoice_table(self) -> Table:
        table = Table()
        table.add_row("Seller", self.order.seller.name)
        table.add_row("Seller address", self.order.seller.address)
        table.add_row()
        table.add_row("Buyer", self.order.buyer.name)
        table.add_row("Buyer address", self.order.buyer.address)
        table.add_row()
        table.add_row("Order ID", self.order.id)
        datetimestr = self.order.date.strftime("%Y-%m-%d %H:%M:%S")
        table.add_row("Order date", datetimestr)
        return table

    def print(self):
        console = Console()
        console.print()
        title_panel = Panel(f"[bold]Invoice[/bold]", SQUARE, expand=False)
        console.print(title_panel, justify="center")
        console.print()
        console.print(f"[bold]Seller:[/bold] {self.order.seller.name}")
        seller_address = self.order.seller.address
        console.print(f"[bold]Seller address:[/bold] {seller_address}")
        console.print()
        console.print(f"[bold]Invoice ID:[/bold] {self.invoice_id}")
        console.print()
        console.print(f"[bold]Order ID:[/bold] {self.order.id}")
        datetimestr = self.order.date.strftime("%Y-%m-%d %H:%M:%S")
        console.print(f"[bold]Order date:[/bold] {datetimestr}")
        console.print(f"[bold]Buyer:[/bold] {self.order.buyer.name}")
        buyer_address = self.order.buyer.address
        console.print(f"[bold]Buyer address:[/bold] {buyer_address}")
        console.print()
        console.print(self.order.get_products_table())
        console.print()
