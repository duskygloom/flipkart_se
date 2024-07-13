from typing import Dict, Literal

from rich.box import SQUARE
from rich.panel import Panel

from functools import partial

from utils.styles import *
from utils.actions import *
from utils.console import *

categories_metadata_t = Literal["description", "usage", "action"]

categories_t = Dict[str, Dict[str, categories_metadata_t]]

app_name = "Flipkart"

app_description = "Command line interface for dummy flipkart."


def get_usage(category: str, subcategory: str, args: str = "") -> str:
    styles = get_styles()
    return f"[{styles['category_title']}]{category}[/] [{styles['category_subtitle']}]{subcategory}[/] {args}"


app_categories: categories_t = {
    "product": {
        "add": {
            "description": "Add a product to cart.",
            "usage": get_usage("product", "add", "(product_id)"),
            "action": Actions.product_add
        },
        "sell": {
            "description": "Sell a product.",
            "usage": get_usage("product", "sell"),
            "action": Actions.product_sell
        },
        "search": {
            "description": "Search for a product.",
            "usage": get_usage("product", "search", "(query)"),
            "action": Actions.product_search
        }
    },
    "account": {
        "create": {
            "description": "Create a new account.",
            "usage": get_usage("account", "create"),
            "action": Actions.account_create
        },
        "details": {
            "description": "See your account details.",
            "usage": get_usage("account", "details"),
            "action": Actions.account_details
        },
        "login": {
            "description": "Log into your account.",
            "usage": get_usage("account", "login", "(username)"),
            "action": Actions.account_login
        },
        "logout": {
            "description": "Log out of your account.",
            "usage": get_usage("account", "logout"),
            "action": Actions.account_logout
        },
        "update": {
            "description": "Update your account details.",
            "usage": get_usage("action", "update", "(address|contact|password)"),
            "action": Actions.account_update
        }
    },
    "transaction": {
        "pending": {
            "description": "List pending transactions.",
            "usage": get_usage("transaction", "pending"),
            "action": Actions.transaction_pending
        },
        "complete": {
            "description": "Complete pending transactions.",
            "usage": get_usage("transaction", "complete"),
            "action": Actions.transaction_complete
        },
        "history": {
            "description": "List history.",
            "usage": get_usage("transaction", "history", "(bought|sold)"),
            "action": Actions.transaction_history
        }
    },
    "setup": {
        "full": {
            "description": "Primary + secondary + optional setup",
            "usage": get_usage("setup", "full"),
            "action": Actions.setup_full
        },
        "required": {
            "description": "Primary + secondary setup",
            "usage": get_usage("setup", "required"),
            "action": Actions.setup_required
        },
        "primary": {
            "description": "Database creation, requires root mysql accout.",
            "usage": get_usage("setup", "primary"),
            "action": Actions.setup_primary
        },
        "secondary": {
            "description": "Table creation.",
            "usage": get_usage("setup", "secondary"),
            "action": Actions.setup_secondary
        },
        "optional": {
            "description": "Populate database with dummy values.",
            "usage": get_usage("setup", "optional"),
            "action": Actions.setup_optional
        },
        "reset_data": {
            "description": "Reset data.",
            "usage": get_usage("setup", "reset_data"),
            "action": Actions.setup_reset_data
        }
    }
}


class App:
    def __init__(self, name: str, description: str, categories: categories_t):
        self.name = name
        self.description = description
        self.categories = categories
        self.console = console
        self.max_category_length = 0
        for i in self.categories:
            for j in self.categories[i]:
                if len(j) > self.max_category_length:
                    self.max_category_length = len(j)

    @staticmethod
    def get_default() -> "App":
        return App(app_name, app_description, app_categories)

    def print_help(self):
        styles = get_styles()
        self.console.print(f"[{styles['app_title']}]Name: [/][{styles['app_body']}]{self.name}")
        self.console.print(f"[{styles['app_title']}]Description: [/][{styles['app_body']}]{self.description}")
        self.console.print()
        self.console.print(f"[{styles['app_title']}]Categories:")
        for category in self.categories:
            content = ""
            for subcategory in self.categories[category]:
                content += f"[{styles['category_subtitle']}]{subcategory}[/]"
                content += f"{' ' * (self.max_category_length - len(subcategory) + 2)}"
                content += f"{self.categories[category][subcategory]['description']}\n"
                content += f"{' ' * (self.max_category_length + 2)}{self.categories[category][subcategory]['usage']}\n"
            if len(content) > 0:
                content = content.rstrip('\n')
            panel = Panel(content, title=f"[{styles['category_title']}]{category}[/]", box=SQUARE, title_align="center")
            self.console.print(panel)

    def parse_args(self, args: list[str]) -> bool:
        if len(args) < 3:
            return False
        if not args[1] in self.categories:
            return False
        if not args[2] in self.categories[args[1]]:
            return False
        self.categories[args[1]][args[2]]["action"](*args[3:])
        return True


__all__ = [
    "App"
]
