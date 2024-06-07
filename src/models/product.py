tax_percent = 0.16

class Product:
    title: str
    cost_price: float
    sell_price: float
    discount: float

    def __init__(self, title: str, cost_price: float, sell_price: float, discount: float) -> None:
        self.title = title
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.discount = discount

    def get_tax_amount(self) -> float:
        return (self.sell_price - self.discount) * tax_percent
    
    def get_total_amount(self) -> float:
        return (self.sell_price - self.discount) * (1 + tax_percent)
