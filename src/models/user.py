from utils.sql import *


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

    @staticmethod
    def from_name(name: str) -> "User":
        '''
        Returns
        -------
        Returns user corresponding to name.
        Returns None if no user found.
        '''
        sql = SQL.get_default()
        sql.execute(f"select username, address, contact from accounts where username = '{name}'")
        return User.from_tuple(sql.fetchone())


_all__ = [
    "User"
]
