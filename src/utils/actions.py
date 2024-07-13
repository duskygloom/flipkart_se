from rich.prompt import Prompt

from utils.styles import *
from utils.console import *

from models.store import *
from models.account_manager import *

from database.setup import *


class Actions:
    @staticmethod
    def product_buy(*args):
        if len(args) <= 0:
            console.print_error("Product ID has not been specified.")
            return
        product_id = args[0]
        store = Store()
        invoice = store.buy(product_id)
        if invoice:
            console.print(invoice)

    @staticmethod
    def product_sell(*args):
        store = Store()
        if store.sell():
            console.print("Product added successfully.")
        else:
            console.print_error("Product could not be added.")

    @staticmethod
    def product_search(*args):
        if len(args) <= 0:
            console.print_error("No query has been searched.")
            return
        query = " ".join(args)
        store = Store()
        results = store.search(query)
        show_next = 'y'
        while show_next == 'y':
            try:
                console.print(next(results))
                show_next = Prompt.ask("Continue", choices=['y', 'n'])
            except StopIteration:
                console.print_error("No product found.")
                show_next = 'n'

    @staticmethod
    def account_create(*args):
        styles = get_styles()
        username = Prompt.ask("Username")
        while AccountManager.user_exists(username):
            console.print(f"User [{styles['highlight']}]{username}[/] already exists.")
            username = Prompt.ask("Username")
        password = Prompt.ask("Password", password=True)
        if AccountManager.create_user(username, password):
            console.print(f"User [{styles['highlight']}]{username}[/] created successfully.")
        else:
            console.print_error(f"User [/][{styles['highlight']}]{username}[/] could not be created.")

    @staticmethod
    def account_details(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print_warning("Log into your account to check your account details.")
            return
        console.print(AccountManager.get_account_details(user))

    @staticmethod
    def account_change_address(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print_warning("Log into your account to change your address.")
            return
        address = Prompt.ask("Address")
        password = Prompt.ask("Password", password=True)
        styles = get_styles()
        if AccountManager.change_address(user.name, password, address):
            console.print(f"Address changed for user [{styles['highlight']}]{user.name}[/]")
        else:
            console.print_error("Failed to change address.")
    
    @staticmethod
    def account_change_contact(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print("Log into your account to change your contact.")
            return
        contact = Prompt.ask("Contact")
        password = Prompt.ask("Password", password=True)
        styles = get_styles()
        if AccountManager.change_contact(user.name, password, contact):
            console.print(f"Contact changed for user [{styles['highlight']}]{user.name}[/].")
        else:
            console.print_error("Failed to change contact.")
    
    @staticmethod
    def account_change_password(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print_warning("Log into your account to change your contact.")
            return
        repeat = True
        while repeat:
            password = Prompt.ask("New password", password=True)
            repassword = Prompt.ask("Repeat password", password=True)
            if password == repassword:
                repeat = False
            else:
                console.print_warning("Passwords do not match.")
        styles = get_styles()
        if AccountManager.change_password(user.name, password):
            console.print(f"Password changed for [{styles['highlight']}]{user.name}[/].")
        else:
            console.print_error("Failed to change password.")

    @staticmethod
    def account_login(*args):
        if len(args) < 1:
            console.print_warning("Username was not provided.")
            return
        username = args[0]
        styles = get_styles()
        password = Prompt.ask("Password", password=True)
        if AccountManager.login(username, password):
            console.print(f"Logged in as [{styles['highlight']}]{username}[/]")
        else:
            console.print_error(f"Could not log in as [/][{styles['highlight']}]{username}[/]")

    @staticmethod
    def account_logout(*args):
        styles = get_styles()
        user = AccountManager.logged_user()
        if user and AccountManager.logout():
            console.print(f"Logged out of [{styles['highlight']}]{user.name}[/]")
        elif user:
            console.print_error(f"Could not log out of [/][{styles['highlight']}]{user.name}[/]")
        else:
            console.print_warning("No account was logged in.")

    @staticmethod
    def setup_full(*args):
        Actions.setup_primary()
        Actions.setup_secondary()
        Actions.setup_optional()

    @staticmethod
    def setup_required(*args):
        Actions.setup_primary()
        Actions.setup_secondary()

    @staticmethod
    def setup_primary(*args):
        if primary_setup():
            console.print_warning("Primary setup successful.")
        else:
            console.print_error("Primary setup unsuccessful.")

    @staticmethod
    def setup_secondary(*args):
        if secondary_setup():
            console.print_warning("Secondary setup successful.")
        else:
            console.print_error("Secondary setup unsuccessful.")

    @staticmethod
    def setup_optional(*args):
        if optional_setup():
            console.print_warning("Optional setup successful.")
        else:
            console.print_error("Optional setup unsuccessful.")

    @staticmethod
    def setup_reset_data(*args):
        table = ""
        if len(args) > 0:
            table = args[0]
        if reset_data(table):
            console.print_warning("Data reset successful.")
        else:
            console.print_error("Could not reset data.")


__all__ = [
    "Actions"
]
