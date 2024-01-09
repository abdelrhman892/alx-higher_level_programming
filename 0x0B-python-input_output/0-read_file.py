#!/usr/bin/python3
"""None"""


def read_file(filename=""):
    """None"""
    with open(filename, encoding='utf-8') as file1:
        print(file1.read(), end="")
