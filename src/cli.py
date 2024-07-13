import sys

from utils.app import *
from utils.styles import *
from utils.console import *


def main():
    args = sys.argv
    app = App.get_default()
    if not app.parse_args(args):
        app.print_help()


if __name__ == "__main__":
    # sys.tracebacklimit = 0
    styles = get_styles()
    try:
        main()
    except KeyboardInterrupt:
        console.print(f"\n[{styles['error']}]Exiting.")
