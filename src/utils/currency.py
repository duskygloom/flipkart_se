def get_currency_string(value: float, currency_char: str = "₹") -> str:
    return f"{currency_char}{value:.2f}"
