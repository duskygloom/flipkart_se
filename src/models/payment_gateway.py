from enum import Enum

from models.order import Order
from models.invoice import Invoice
from models.product import Product


class PaymentMode(Enum):
    upi = 0
    cash = 1
    card = 2


class PaymentGateway:
    mode: PaymentMode
    order: Order

    def process_payment(self):
        ...

    def get_invoice(self, invoice_id: str) -> Invoice:
        return Invoice(invoice_id, self.order)
