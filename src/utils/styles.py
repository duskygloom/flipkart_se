import os
import json

from typing import Literal, Dict

styles_file = "styles.json"
styles_encoding = "utf-8"

sub_styles_t = Literal[
    "app_title_style",
    "app_body_style",
    "category_title_style",
    "category_subtitle_style",
    "warning_title_style",
    "warning_body_style",
    "error_title_style",
    "error_body_style"
]

styles_t = Dict[sub_styles_t, str]


def get_styles() -> styles_t:
    '''
    Info
    ----
    Parses styles json file.

    Returns
    -------
    Returns parsed Dictionary.
    Returns empty Dictionary if config file is not found.
    '''
    if not os.path.isfile(styles_file):
        return {}

    with open(styles_file, "r", encoding=styles_encoding) as fp:
        styles_data = json.load(fp)
        fp.close()
        return styles_data


def save_styles(styles_data: styles_t):
    '''
    Info
    ----
    Saves styles_data to config json file.
    '''
    with open(styles_file, "w", encoding=styles_encoding) as fp:
        json.dump(styles_data, fp, ensure_ascii=False, indent="\t")


__all__ = [
    "get_styles",
    "save_styles"
]
