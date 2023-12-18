#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int(value)
        print("{}".format(value))
        return True
    except ValueError:
        return False
