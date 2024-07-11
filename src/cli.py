import sys

from rich.console import Console

from utils.app import *
from utils.config import *

config = get_config()

console = Console()

app = App.get_default(console)


def setup_console(console: Console):
    if console.width > config["screen_width"]:
        console.width = config["screen_width"]


def setup():
    setup_console(console)


def main():
    args = sys.argv
    if not app.parse_args(args):
        app.print_help()


if __name__ == "__main__":
    setup()
    main()
