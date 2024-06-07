from datetime import datetime

from rich.box import SQUARE
from rich.table import Table

from utils.currency import get_currency_string

from models.buyer import Buyer
from models.seller import Seller
from models.product import Product

shipment_charge = 40
shipment_charge_exemption_price = 500

class Order:
    id: str
    date: datetime
    buyer: Buyer
    seller: Seller
    product_qty: dict[Product, int]

    def __init__(self, id: str, date: datetime, buyer: Buyer, seller: Seller, product_qty: dict[Product, int] = {}) -> None:
        self.id = id
        self.date = date
        self.buyer = buyer
        self.seller = seller
        self.product_qty = product_qty

    def add_product_qty(self, product: Product, qty: int = 1) -> None:
        if product in self.product_qty:
            self.product_qty[product] += qty
        else:
            self.product_qty[product] = qty

    def get_gross_amount(self) -> float:
        '''
        Returns
        -------
        Cost of all the products in the order but does not include shipment charge.
        '''
        total = 0
        for product in self.product_qty:
            total += product.get_total_amount() * self.product_qty[product]
        return total

    def get_shipment_charge(self) -> float:
        if self.get_gross_amount() < shipment_charge_exemption_price:
            return shipment_charge
        return 0
    
    def get_total_amount(self) -> float:
        '''
        Returns
        -------
        Cost of all the products in the order and also includes shipment charge.
        '''
        return self.get_gross_amount() + self.get_shipment_charge()
    
    def get_products_table(self) -> Table:
        table = Table(box=SQUARE, show_lines=True)
        table.add_column("Title")
        table.add_column("Qty", justify="right")
        table.add_column("Amount", justify="right")
        table.add_column("Discount", justify="right")
        table.add_column("Tax", justify="right")
        table.add_column("Total", justify="right")
        for product in self.product_qty:
            qty = self.product_qty[product]
            table.add_row(
                product.title,
                str(qty),
                get_currency_string(product.sell_price*qty),
                get_currency_string(product.discount*qty),
                get_currency_string(product.get_tax_amount()*qty),
                get_currency_string(product.get_total_amount()*qty)
            )
        table.add_row("Shipment", "", "", "", get_currency_string(self.get_shipment_charge()))
        table.add_row("Grand total", "", "", "", "", get_currency_string(self.get_total_amount()), style="bold")
        return table
