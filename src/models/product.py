class Product:
    product_id: int
    name: str
    keywords: list[str]
    description: str
    price: float
    discount: float

    def __init__(self, product_id: int, name: str, keywords: str, description: str, price: float, discount: float):
        self.product_id = product_id
        self.name = name
        self.keywords = keywords.split(',')
        self.description = description
        self.price = price
        self.discount = discount

    @staticmethod
    def from_tuple(row: tuple) -> "Product":
        if len(row) < 6:
            return None
        return Product(row[0], row[1], row[2], row[3], row[4], row[5])


__all__ = [
    "Product"
]
