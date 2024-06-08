from models.order import Order
from models.buyer import Buyer
from models.seller import Seller
from models.product import Product
from models.payment_gateway import Invoice

from datetime import datetime

buyer = Buyer("Hans", "Kolkata")
seller = Seller("Flipkart", "Mumbai")
order = Order("Order1", datetime.now(), buyer, seller)
order.add_product_qty(Product("5 year old", 500, 1000, 150))
order.add_product_qty(Product("Milk", 40, 80, 10), 4)

invoice = Invoice("Invoice1", order)

invoice.print()
