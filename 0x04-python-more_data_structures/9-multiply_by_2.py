#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {}

    for key, value in a_dictionary.items():
        if isinstance(value, (int, float)):
            b_dictionary[key] = value * 2
        else:
            return None

    return b_dictionary
