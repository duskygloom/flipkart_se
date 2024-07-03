from typing import Dict, Literal

from rich.console import Console
from rich.panel import Panel
from rich.box import SQUARE

from functools import partial

from utils.styles import *

# styles: will be moved to styles.json later

styles = get_styles()

app_title_style = "bold yellow"
app_body_style = "white"
category_title_style = "bold blue"
category_subtitle_style = "yellow"

categories_metadata_t = Literal["description", "usage", "action"]

categories_t = Dict[str, Dict[str, categories_metadata_t]]

app_name = "Flipkart"

app_description = "Command line interface for dummy flipkart."

app_categories: categories_t = {
    "product": {
        "buy": {
            "description": "Buy a product.",
            "usage": f"[{category_title_style}]product[/] [{category_subtitle_style}]buy[/] <product_id>",
            "action": partial(print, "buy")
        },
        "sell": {
            "description": "Sell a product.",
            "usage": f"[{category_title_style}]product[/] [{category_subtitle_style}]sell[/]",
            "action": partial(print, "sell")
        },
        "search": {
            "description": "Search for a product.",
            "usage": f"[{category_title_style}]product[/] [{category_subtitle_style}]search[/] <query>",
            "action": partial(print, "search")
        }
    },
    "account": {
        "create": {
            "description": "Create a new account.",
            "usage": f"[{category_title_style}]account[/] [{category_subtitle_style}]create[/]",
            "action": partial(print, "create")
        },
        "login": {
            "description": "Log into your account.",
            "usage": f"[{category_title_style}]account[/] [{category_subtitle_style}]login[/]",
            "action": partial(print, "login")
        },
        "logout": {
            "description": "Log out of your account.",
            "usage": f"[{category_title_style}]account[/] [{category_subtitle_style}]logout[/]",
            "action": partial(print, "logout")
        }
    },
    "orders": {
        "pending": {
            "description": "List pending orders.",
            "usage": f"[{category_title_style}]orders[/] [{category_subtitle_style}]pending[/]",
            "action": partial(print, "pending")
        },
        "past": {
            "description": "List past orders.",
            "usage": f"[{category_title_style}]orders[/] [{category_subtitle_style}]past[/] <year>",
            "action": partial(print, "past")
        }
    }
}

class App:
    def __init__(self, name: str, description: str, categories: categories_t, console: Console):
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
    def get_default(console: Console) -> "App":
        return App(app_name, app_description, app_categories, console)
    
    def print_help(self):
        self.console.print(f"[{app_title_style}]Name: [/][{app_body_style}]{self.name}")
        self.console.print(f"[{app_title_style}]Description: [/][{app_body_style}]{self.description}")
        self.console.print()
        self.console.print(f"[{app_title_style}]Categories:")
        for category in self.categories:
            content = ""
            for subcategory in self.categories[category]:
                content += f"[{category_subtitle_style}]{subcategory}[/]"
                content += f"{' ' * (self.max_category_length - len(subcategory) + 2)}"
                content += f"{self.categories[category][subcategory]['description']}\n"
                content += f"{' ' * (self.max_category_length + 2)}{self.categories[category][subcategory]['usage']}\n"
            if len(content) > 0:
                content = content.rstrip('\n')
            panel = Panel(content, title=f"[{category_title_style}]{category}[/]", box=SQUARE, title_align="center")
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
