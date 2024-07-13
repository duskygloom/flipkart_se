class User:
    name: str
    address: str

    def __init__(self, name: str, address: str, contact: str):
        self.name = name
        self.address = address
        self.contact = contact

    @staticmethod
    def from_tuple(row: tuple) -> "User":
        if not row or len(row) < 3:
            return None
        return User(row[0], row[1], row[2])


class Buyer(User):
    ...


class Seller(User):
    ...


_all__ = [
    "Buyer",
    "Seller"
]
