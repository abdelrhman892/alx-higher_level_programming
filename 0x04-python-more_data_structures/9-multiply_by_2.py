#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary = a_dictionary.copy()
    b_dictionary = a_dictionary
    b_dictionary.update((key, value * 2) for key, value in b_dictionary.items())
    return b_dictionary
