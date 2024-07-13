from utils.sql import *
from utils.config import *
from utils.styles import *

from rich.box import SQUARE
from rich.panel import Panel

from models.user import *


class AccountManager:
    @staticmethod
    def login(username: str, password: str) -> bool:
        '''
        Description
        -----------
        Logs in and returns status.
        '''
        sql = SQL.get_default()
        sql.execute(f"select username, address, contact from accounts where username = '{username}' and password = '{password}'")
        user = User.from_tuple(sql.fetchone())
        if not user:
            return False
        config = get_config()
        config['current_user'] = user.name
        save_config(config)
        return True
    
    @staticmethod
    def user_exists(name: str) -> bool:
        '''
        Returns
        -------
        Returns True if name exists in database.
        Else returns False.
        '''
        sql = SQL.get_default()
        sql.execute("select username from accounts")
        return (name,) in sql.fetchall()
    
    @staticmethod
    def create_user(username: str, password: str) -> bool:
        '''
        Description
        -----------
        Creates a new user account and returns status.
        '''
        sql = SQL.get_default()
        return sql.execute(f"insert into accounts (username, password) values ('{username}', '{password}')", commit=True)
    
    @staticmethod
    def get_account_details(user: User) -> Panel:
        styles = get_styles()
        panel_text = f"[{styles['app_title']}]Name[/]{7*' '}[{styles['app_body']}]{user.name}[/]\n"
        panel_text += f"[{styles['app_title']}]Address[/]{4*' '}[{styles['app_body']}]{user.address}[/]\n"
        panel_text += f"[{styles['app_title']}]Contact[/]{4*' '}[{styles['app_body']}]{user.contact}[/]"
        panel = Panel(panel_text, box=SQUARE, title=f"[{styles['highlight']}]Account details[/]")
        return panel
    
    @staticmethod
    def change_address(username: str, password: str, address: str) -> bool:
        '''
        Description
        -----------
        Changes address for a user and returns status.
        '''
        sql = SQL.get_default()
        return sql.execute(f"update accounts set address = '{address}' where username = '{username}'", commit=True)
    
    @staticmethod
    def change_contact(username: str, password: str, contact: str) -> bool:
        '''
        Description
        -----------
        Changes contact for a user and returns status.
        '''
        sql = SQL.get_default()
        return sql.execute(f"update accounts set contact = '{contact}' where username = '{username}'", commit=True)
    
    @staticmethod
    def change_password(username: str, newpassword: str) -> bool:
        '''
        Description
        -----------
        Changes password for username.
        No two factor authentication during password change.
        '''
        sql = SQL.get_default()
        return sql.execute(f"update accounts set password = '{newpassword}' where username = '{username}'", commit=True)
    
    @staticmethod
    def logged_user() -> User:
        '''
        Returns
        -------
        Returns the user who is currently logged in.
        Returns None if no one is logged in.
        '''
        config = get_config()
        if not config['current_user']:
            return None
        sql = SQL.get_default()
        sql.execute(f"select username, address, contact from accounts where username = '{config['current_user']}'")
        user = User.from_tuple(sql.fetchone())
        if not user:
            config['current_user'] = ""
            save_config(config)
        return user
    
    @staticmethod
    def logout() -> bool:
        '''
        Description
        -----------
        Logs out and returns status.
        '''
        config = get_config()
        if AccountManager.logged_user():
            config['current_user'] = ""
            return True
        return False


__all__ = [
    "AccountManager"
]
