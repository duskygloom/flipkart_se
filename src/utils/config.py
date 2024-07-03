import os
import json

from typing import Literal, Dict

config_file = "config.json"
config_encoding = "utf-8"

subconfig_t = Literal["screen_width", "results_per_page"]

config_t = Dict[subconfig_t, str]


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
