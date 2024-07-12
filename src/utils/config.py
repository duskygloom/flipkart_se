import os
import json

from typing import TypedDict

config_file = "config.json"
config_encoding = "utf-8"

class config_t(TypedDict):
    root_username: str
    root_password: str
    screen_width: int
    result_per_page: int
    mysql_username: str
    mysql_password: str
    mysql_hostname: str
    mysql_database: str
    current_user: str


def get_config() -> config_t:
    '''
    Info
    ----
    Parses config json file.

    Returns
    -------
    Returns parsed Dictionary.
    Returns empty Dictionary if config file is not found.
    '''
    if not os.path.isfile(config_file):
        return {}

    with open(config_file, "r", encoding=config_encoding) as fp:
        config_data = json.load(fp)
        fp.close()
        return config_data


def save_config(config_data: config_t):
    '''
    Info
    ----
    Saves config_dict to config json file.
    '''
    with open(config_file, "w", encoding=config_encoding) as fp:
        json.dump(config_data, fp, ensure_ascii=False, indent="\t")


__all__ = [
    "get_config",
    "save_config"
]
