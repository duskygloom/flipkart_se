from datetime import datetime


def get_current_strftime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_strftime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_datetime(isotime: str) -> datetime:
    return datetime.fromisoformat(isotime)


__all__ = [
    "get_current_strftime",
    "get_strftime",
    "get_datetime"
]
