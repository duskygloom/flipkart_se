from enum import Enum

from rich.box import SQUARE
from rich.panel import Panel
from rich.table import Table

from models.order import Order
from models.console import console
from models.product import Product


class PaymentMode(Enum):
    upi = 0
    cash = 1
    card = 2


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
        table.add_row("Order date", self.order.date.strftime('%Y-%m-%d %H:%M:%S'))
        return table

    def print(self):
        console.print()
        console.print(Panel(f"[bold]Invoice[/bold]", SQUARE, expand=False))
        console.print()
        console.print(f"[bold]Seller:[/bold] {self.order.seller.name}")
        console.print(f"[bold]Seller address:[/bold] {self.order.seller.address}")
        console.print()
        console.print(f"[bold]Invoice ID:[/bold] {self.invoice_id}")
        console.print()
        console.print(f"[bold]Order ID:[/bold] {self.order.id}")
        console.print(f"[bold]Order date:[/bold] {self.order.date.strftime('%Y-%m-%d %H:%M:%S')}")
        console.print(f"[bold]Buyer:[/bold] {self.order.buyer.name}")
        console.print(f"[bold]Buyer address:[/bold] {self.order.buyer.address}")
        console.print()
        console.print(self.order.get_products_table())
        console.print()


class PaymentGateway:
    mode: PaymentMode
    order: Order

    def process_payment(self):
        ...

    def get_invoice(self, invoice_id: str) -> Invoice:
        return Invoice(invoice_id, self.order)
