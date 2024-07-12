class User:
    name: str
    address: str

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    @staticmethod
    def from_tuple(row: tuple) -> "User":
        if len(row) < 2:
            return None
        return User(row[0], row[1])


class Buyer(User):
    ...


class Seller(User):
    ...


_all__ = [
    "Buyer",
    "Seller"
]
