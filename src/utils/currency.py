from utils.styles import *

def get_currency_string(value: float, currency_char: str = "₹") -> str:
    styles = get_styles()
    return f"[{styles['highlight']}]{currency_char}{value:.2f}"


__all__ = [
    "get_currency_string"
]
