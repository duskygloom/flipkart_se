class Product:
    title: str
    cost_price: float
    sell_price: float
    discount: float
    tax_percent: float = 0.16

    def __init__(self, title: str, cost_price: float, sell_price: float,
                 discount: float) -> None:
        self.title = title
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.discount = discount

    def get_tax_amount(self) -> float:
        return (self.sell_price - self.discount) * self.tax_percent

    def get_total_amount(self) -> float:
        return (self.sell_price - self.discount) * (1 + self.tax_percent)

__all__ = [
    Product
]
