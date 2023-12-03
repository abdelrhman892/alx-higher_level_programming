#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list = my_list.copy()
    list_result = my_list
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            list_result[i] = True
        else:
            list_result[i] = False
        i += 1
    return list_result
