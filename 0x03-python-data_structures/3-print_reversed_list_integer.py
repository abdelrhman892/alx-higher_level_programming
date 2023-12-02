#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    while count > 0:
        print("{}".format(my_list[count - 1]))
        count -= 1
