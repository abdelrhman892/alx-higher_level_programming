#!/usr/bin/python3
"""
    None
"""


import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file using JSON
    """
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)
