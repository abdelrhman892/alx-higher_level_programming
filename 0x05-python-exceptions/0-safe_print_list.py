#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            if i == x - 1:
                print(my_list[i])
                i += 1
            else:
                print(my_list[i], end='')
                i += 1
    except IndexError:
        x = len(my_list)
        print("")
    return x
