import mysql.connector as sql
from mysql.connector.abstracts import MySQLCursorAbstract, MySQLConnectionAbstract

from utils.config import *
from utils.console import *


class SQL:
    cursor: MySQLCursorAbstract
    connection: MySQLConnectionAbstract

    history: str = "database/history.sql"

    def __init__(self, username: str, password: str, hostname: str = "localhost", database: str = "") -> MySQLConnectionAbstract:
        '''
        Description
        -----------
        Connects to a database using username, password, hostname and database.

        Returns
        -------
        Returns connection object if successfully connected, else returns None.
        '''
        try:
            self.connection = sql.connect(
                user=username,
                password=password,
                host=hostname,
                database=database
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            logger.error(f"Cannot connect to {database} database using {username}")
            self.connection = self.cursor = None

    def __del__(self):
        '''
        Description
        -----------
        Destructor of this class.
        Closes SQL connection.
        '''
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
    
    def __bool__(self):
        '''
        Description
        -----------
        Determines whether the class is True or False.
        Useful for using boolean operations.
        '''
        return self.connection != None

    def execute(self, query: str, commit: bool = False) -> bool:
        '''
        Description
        -----------
        Executes query and also handles error.

        Returns
        -------
        Returns True if successfully executed, else returns False.
        '''
        try:
            self.cursor.execute(query)
            with open(self.history, "a") as fp:
                fp.write(query + ";\n")
            if commit:
                self.connection.commit()
        except Exception as e:
            logger.error(e)
            return False
        return True
    
    def commit(self):
        if not self.connection:
            return
        self.connection.commit()

    def rollback(self):
        if not self.connection:
            return
        self.connection.rollback()
    
    def fetchone(self) -> tuple:
        if not self.cursor:
            return []
        return self.cursor.fetchone()
    
    def fetchmany(self, size: int = 1) -> list[tuple]:
        if not self.cursor:
            return []
        return self.cursor.fetchmany(size)
    
    def fetchall(self) -> list[tuple]:
        if not self.cursor:
            return []
        return self.cursor.fetchall()
    
    @staticmethod
    def get_default() -> "SQL":
        config = get_config()
        return SQL(config['mysql_username'], config['mysql_password'], config['mysql_hostname'], config['mysql_database'])


__all__ = [
    "SQL"
]
