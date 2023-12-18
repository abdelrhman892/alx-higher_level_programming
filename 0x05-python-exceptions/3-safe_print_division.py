#!/usr/bin/python3
def safe_print_division(a, b):
    if b == 0:
        result = None
    else:
        result = a / b
    try:
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        return result
