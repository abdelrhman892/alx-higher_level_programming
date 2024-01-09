#!/usr/bin/python3
"""
    None
"""


import json


def load_from_json_file(filename):
    """
        loads an object to from JSON
    """
    with open(filename, "r") as js_file:
        my_obj = json.load(js_file)
        return my_obj
