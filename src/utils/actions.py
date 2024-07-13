from rich.prompt import Prompt

from utils.styles import *
from utils.console import *

from models.user import *
from models.store import *
from models.account_manager import *

from database.setup import *


def transaction_bought_history():
    user = AccountManager.logged_user()
    if not user:
        console.print_warning("Log into your account to check your bought history.")
    store = Store()
    table = store.get_bought_history(user)
    if table and table.row_count > 0:
        console.print(table)
    else:
        console.print("Nothing bought.")


def transaction_sold_history():
    user = AccountManager.logged_user()
    if not user:
        console.print_warning("Log into your account to check your sold history.")
    store = Store()
    table = store.get_sold_history(user)
    if table and table.row_count > 0:
        console.print(table)
    else:
        console.print("Nothing sold.")


def account_update_address():
    user = AccountManager.logged_user()
    if not user:
        console.print_warning("Log into your account to change your address.")
        return
    address = Prompt.ask("Address")
    styles = get_styles()
    if AccountManager.change_address(user.name, address):
        console.print(f"Address changed for user [{styles['highlight']}]{user.name}[/]")
    else:
        console.print_error("Failed to change address.")


def account_update_contact():
    user = AccountManager.logged_user()
    if not user:
        console.print("Log into your account to change your contact.")
        return
    contact = Prompt.ask("Contact")
    styles = get_styles()
    if AccountManager.change_contact(user.name, contact):
        console.print(f"Contact changed for user [{styles['highlight']}]{user.name}[/].")
    else:
        console.print_error("Failed to change contact.")


def account_update_password():
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


class Actions:
    @staticmethod
    def product_add(*args):
        if len(args) <= 0:
            console.print_error("Product ID has not been specified.")
            return
        product_id = args[0]
        store = Store()
        if store.add_to_cart(product_id):
            console.print_warning(f"Product {product_id} has been added to cart.")
        else:
            console.print_error(f"Could not add product {product_id} to cart.")

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
        if results and results.row_count > 0:
            console.print(results)
        else:
            console.print_error("No product found.")

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
            console.print_error(f"User [{styles['highlight']}]{username}[/] could not be created.")

    @staticmethod
    def account_details(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print_warning("Log into your account to check your account details.")
            return
        console.print(AccountManager.get_account_details(user))

    @staticmethod
    def account_update(*args):
        styles = get_styles()
        options = ["address", "contact", "password"]
        if len(args) < 1 or args[0] not in options:
            console.print(f"Choose between [{styles['highlight']}]{options[0]}[/], [{styles['highlight']}]{options[1]}[/] and [{styles['highlight']}]{options[2]}[/] history.")
        elif args[0] == options[0]:
            account_update_address()
        elif args[0] == options[1]:
            account_update_contact()
        elif args[0] == options[2]:
            account_update_password()

    @staticmethod
    def account_login(*args):
        if len(args) < 1:
            console.print_warning("Username was not provided.")
            return
        username = args[0]
        styles = get_styles()
        if not User.from_name(username):
            console.print(f"User [{styles['highlight']}]{username}[/] does not exist.")
            return
        password = Prompt.ask("Password", password=True)
        if AccountManager.login(username, password):
            console.print(f"Logged in as [{styles['highlight']}]{username}[/]")
        else:
            console.print_error(f"Could not log in as [{styles['highlight']}]{username}[/]")

    @staticmethod
    def account_logout(*args):
        styles = get_styles()
        user = AccountManager.logged_user()
        if user and AccountManager.logout():
            console.print(f"Logged out of [{styles['highlight']}]{user.name}[/]")
        elif user:
            console.print_error(f"Could not log out of [{styles['highlight']}]{user.name}[/]")
        else:
            console.print_warning("No account was logged in.")

    @staticmethod
    def transaction_pending(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print_warning("Log into your account to check your pending transactions.")
        store = Store()
        table = store.get_cart(user)
        if table and table.row_count > 0:
            console.print(table)
        else:
            console.print("Empty cart.")
    
    @staticmethod
    def transaction_complete(*args):
        user = AccountManager.logged_user()
        if not user:
            console.print_warning("Log into your account to complete your pending transactions.")
        store = Store()
        invoice = store.buy(user)
        if invoice:
            invoice.print()
        else:
            console.print("Nothing bought.")

    @staticmethod
    def transaction_history(*args):
        styles = get_styles()
        options = ["bought", "sold"]
        if len(args) < 1 or args[0] not in options:
            console.print(f"Choose between [{styles['highlight']}]{options[0]}[/] and [{styles['highlight']}]{options[1]}[/] history.")
        elif args[0] == options[0]:
            transaction_bought_history()
        elif args[0] == options[1]:
            transaction_sold_history()
        

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
