#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) + len(tuple_b) == 0:
        return None
    elif len(tuple_a) == 0:
        el1 = 0 + tuple_b[0]
        el2 = 0 + tuple_b[1]
    elif len(tuple_b) == 0:
        el1 = 0 + tuple_a[0]
        el2 = 0 + tuple_a[1]

    elif len(tuple_a) == 1:
        el1 = tuple_a[0] + tuple_b[0]
        el2 = 0 + tuple_b[1]
    elif len(tuple_b) == 1:
        el1 = tuple_a[0] + tuple_b[0]
        el2 = 0 + tuple_a[1]
    else:
        el1 = tuple_a[0] + tuple_b[0]
        el2 = tuple_a[1] + tuple_b[1]
    new_tuple = (el1, el2)
    return new_tuple
