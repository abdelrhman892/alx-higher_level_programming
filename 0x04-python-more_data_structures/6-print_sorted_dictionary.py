#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        if isinstance(key, str):
            print(f"{key}: {a_dictionary[key]}")
        else:
            return None
