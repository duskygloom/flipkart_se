import sys

from utils.app import *
from utils.config import *
from utils.console import *

from database.setup import *

config = get_config()

app = App.get_default()


def main():
    args = sys.argv
    if not app.parse_args(args):
        app.print_help()


if __name__ == "__main__":
    # sys.tracebacklimit = 0
    main()
