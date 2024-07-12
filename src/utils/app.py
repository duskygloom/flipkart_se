from typing import Dict, Literal

from rich.box import SQUARE
from rich.panel import Panel

from functools import partial

from utils.styles import *
from utils.console import *

from models.store import *

from database.setup import *

styles = get_styles()

categories_metadata_t = Literal["description", "usage", "action"]

categories_t = Dict[str, Dict[str, categories_metadata_t]]

app_name = "Flipkart"

app_description = "Command line interface for dummy flipkart."


def buy(*args):
    if len(args) <= 0:
        logger.error("Product ID has not been specified.")
        return
    product_id = args[0]
    store = Store()
    invoice = store.buy(product_id)
    console.print(invoice)


def primary(*args):
    if primary_setup():
        logger.info("Primary setup successful.")
    else:
        logger.error("Primary setup unsuccessful.")


def secondary(*args):
    if secondary_setup():
        logger.info("Secondary setup successful.")
    else:
        logger.error("Secondary setup unsuccessful.")


def optional(*args):
    if optional_setup():
        logger.info("Optional setup successful.")
    else:
        logger.error("Optional setup unsuccessful.")


def get_usage(category: str, subcategory: str, args: str = "") -> str:
    return f"[{styles['category_title_style']}]{category}[/] [{styles['category_subtitle_style']}]{subcategory}[/] {args}"


app_categories: categories_t = {
    "product": {
        "buy": {
            "description": "Buy a product.",
            "usage": get_usage("product", "buy", "<product_id>"),
            "action": buy
        },
        "sell": {
            "description": "Sell a product.",
            "usage": get_usage("product", "sell"),
            "action": partial(print, "sell")
        },
        "search": {
            "description": "Search for a product.",
            "usage": get_usage("product", "search", "<query>"),
            "action": partial(print, "search")
        }
    },
    "account": {
        "create": {
            "description": "Create a new account.",
            "usage": get_usage("account", "create"),
            "action": partial(print, "create")
        },
        "login": {
            "description": "Log into your account.",
            "usage": get_usage("account", "login"),
            "action": partial(print, "login")
        },
        "logout": {
            "description": "Log out of your account.",
            "usage": get_usage("account", "logout"),
            "action": partial(print, "logout")
        }
    },
    "transactions": {
        "pending": {
            "description": "List pending transactions.",
            "usage": get_usage("transactions", "pending"),
            "action": partial(print, "pending")
        },
        "past": {
            "description": "List past transactions.",
            "usage": get_usage("transactions", "past", "<year>"),
            "action": partial(print, "past")
        }
    },
    "setup": {
        "primary": {
            "description": "Database creation, requires root mysql accout.",
            "usage": get_usage("setup", "primary"),
            "action": primary
        },
        "secondary": {
            "description": "Table creation.",
            "usage": get_usage("setup", "secondary"),
            "action": secondary
        },
        "optional": {
            "description": "Populate database with dummy values.",
            "usage": get_usage("setup", "optional"),
            "action": optional
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
        self.console.print(f"[{styles['app_title_style']}]Name: [/][{styles['app_body_style']}]{self.name}")
        self.console.print(f"[{styles['app_title_style']}]Description: [/][{styles['app_body_style']}]{self.description}")
        self.console.print()
        self.console.print(f"[{styles['app_title_style']}]Categories:")
        for category in self.categories:
            content = ""
            for subcategory in self.categories[category]:
                content += f"[{styles['category_subtitle_style']}]{subcategory}[/]"
                content += f"{' ' * (self.max_category_length - len(subcategory) + 2)}"
                content += f"{self.categories[category][subcategory]['description']}\n"
                content += f"{' ' * (self.max_category_length + 2)}{self.categories[category][subcategory]['usage']}\n"
            if len(content) > 0:
                content = content.rstrip('\n')
            panel = Panel(content, title=f"[{styles['category_title_style']}]{category}[/]", box=SQUARE, title_align="center")
            self.console.print(panel)

    def parse_args(self, args: list[str]) -> bool:
        if len(args) < 3:
            return False
        if not args[1] in self.categories:
            return False
        if not args[2] in self.categories[args[1]]:
            return False
        self.categories[args[1]][args[2]]["action"](args[3:])
        return True


__all__ = [
    "App"
]
