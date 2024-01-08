#!/usr/bin/python3
"""
nothing
"""


def inherits_from(obj, a_class):
    """None"""
    if issubclass(type(obj), a_class) or isinstance(obj, a_class):
        return True
    else:
        return False
