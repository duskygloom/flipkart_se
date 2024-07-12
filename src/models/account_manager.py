from utils.sql import *
from utils.config import *

from models.user import *

config = get_config()


class AccountManager:
    @staticmethod
    def login(username: str, password: str) -> bool:
        '''
        Description
        -----------
        Logs in and returns status.
        '''
        sql = SQL.get_default()
        sql.execute(f"select username, address from accounts where username == '{username}' and password == '{password}'")
        user = User.from_tuple(sql.fetchone())
        if not user:
            return False
        config['current_user'] = user.name
        save_config(config)
        return True
    
    @staticmethod
    def logged_user() -> User:
        '''
        Returns
        -------
        Returns the user who is currently logged in.
        Returns None if no one is logged in.
        '''
        if not config['current_user']:
            return None
        sql = SQL.get_default()
        sql.execute(f"select username, address from accounts where username == '{config['current_user']}'")
        user = User.from_tuple(sql.fetchone())
        return user
    
    @staticmethod
    def logout() -> bool:
        '''
        Description
        -----------
        Logs out and returns status.
        '''
        if AccountManager.is_logged_in():
            config['current_user'] = ""
            return True
        return False


__all__ = [
    "AccountManager"
]
