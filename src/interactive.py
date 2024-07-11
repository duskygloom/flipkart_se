from utils.config import *
from utils.styles import *

from models.store import *

from rich.box import Box
from rich.box import HEAVY
from rich.rule import Rule
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.console import Console
from rich.columns import Columns

# config

config = get_config()
styles = get_styles()

# console setup

console = Console()

if console.width > config["screen_width"]:
    console.width = config["screen_width"]

# box definitions

title_box = Box(
    "━━┳┓\n"
    "  ┃┃\n"
    "━━╋┫\n"
    "  ┃┃\n"
    "━━╋┫\n"
    "━━╋┫\n"
    "  ┃┃\n"
    "━━┻┛\n"
)

# option definitions

main_options = [
    "Buy",
    "Sell",
    "Cart",
    "Account",
    "Exit",
]

# functions

def print_title():
    '''
    Description
    -----------
    Prints title.
    '''
    title_panel = Panel(
        "Flipkart", 
        box=title_box, 
        style=styles["title"], 
        border_style=styles["title_border"], 
        padding=(0, 0)
    )
    console.print(title_panel)
    console.print()

def get_option(options: list) -> int:
    '''
    Description
    -----------
    Shows option to the user.

    Returns
    -------
    The option that user selected.
    '''
    option_columns = Columns(
        [f"{i+1}. {options[i]}" for i in range(len(options))], 
        padding=(0, 2), 
        equal=True, 
        expand=True
    )
    console.print(option_columns)
    console.print()
    option = Prompt.ask(
        "Select an option", 
        console=console,
        choices=[str(i + 1) for i in range(len(options))]
    )
    console.print()
    return int(option) - 1

def get_result_option(upper_limit: int) -> int:
    '''
    Description
    -----------
    Shows prompt for selecting from a set of results.

    Parameters
    ----------
    upper_limit: maximum number of options in the choices
                 in the range [0, upper_limit]

    Returns
    -------
    The option that user selected. 0 is the default value.
    '''
    console.print()
    option = Prompt.ask(
        "Select an option", 
        console=console,
        choices=list[range(upper_limit + 1)],
        show_choices=False,
        default="0",
        show_default=False
    )
    console.print()
    return int(option)

def print_subtitle(subtitle: str):
    '''
    Description
    -----------
    Prints subtitle.
    '''
    subtitle_panel = Panel(
        subtitle, 
        box=title_box, 
        style=styles["subtitle"], 
        border_style=styles["subtitle_border"], 
        padding=(0, 0),
        width=20,
    )
    console.print(subtitle_panel)
    console.print()

def print_headline(headline: str):
    '''
    Description
    -----------
    Prints headline.
    '''
    headline_rule = Rule(
        f"[{styles['subtitle']}]{headline}", 
        characters="━",
        style=styles["subtitle_border"], 
        align="left",
    )
    console.print(headline_rule)
    console.print()


# windows

def buy_window():
    query = Prompt.ask("Search", console=console)
    products = Store.search(query)
    console.print()
    index = 0
    step = config["results_per_page"]
    # implement multiple pages of results

def sell_window():
    ...

def cart_window():
    ...

def account_window():
    ...

def exit_window():
    exit_rule = Rule(
        f"[{styles['exit_text']}]Session ended", 
        characters="━", 
        style=styles["exit_border"]
    )
    console.print(exit_rule)

# main

def main():
    print_title()
    option = get_option(main_options)
    if (option >= 0 and option <= 3):
        print_subtitle(main_options[option])
    if option == 0:
        buy_window()
    elif option == 1:
        sell_window()
    elif option == 2:
        cart_window()
    elif option == 3:
        account_window()
    elif option == 4:
        exit_window()
        return

if __name__ == "__main__":
    main()
