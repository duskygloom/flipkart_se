import logging

from rich.logging import RichHandler
from rich.console import Console as RichConsole

from utils.config import *
from utils.styles import *

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

config = get_config()

logger = logging.getLogger("rich")


class Console(RichConsole):
    def __init__(self):
        super().__init__()

    def print_error(self, text: str):
        styles = get_styles()
        self.print(f"[{styles['error']}]{text}[/]")
    
    def print_warning(self, text: str):
        styles = get_styles()
        self.print(f"[{styles['warning']}]{text}[/]")

screen_width = Console().width

console = Console(width=config['screen_width'] if screen_width > config['screen_width'] else screen_width)


__all__ = [
    "console"
]
