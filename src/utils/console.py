import logging

from rich.console import Console
from rich.logging import RichHandler

from utils.config import *

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

config = get_config()

logger = logging.getLogger("rich")

screen_width = Console().width

console = Console(width=config['screen_width'] if screen_width > config['screen_width'] else screen_width)


__all__ = [
    "console",
    "logger"
]
