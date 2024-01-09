#!/usr/bin/python3
"""None"""
import json


def save_to_json_file(my_obj, filename):
    """None"""
    data = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as jsonFile:
        jsonFile.write(data)
