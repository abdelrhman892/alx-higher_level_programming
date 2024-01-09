#!/usr/bin/python3
"""None"""


def write_file(filename="", text=""):
    """None"""
    numOfChar = 0
    with open(filename, mode= 'w', encoding= 'utf-8') as file:
        file.write(text)
        file.close()

    return len(text)
