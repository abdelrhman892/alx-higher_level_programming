#!/usr/bin/python3
"""None"""


def append_write(filename="", text=""):
    """Appends text to"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
