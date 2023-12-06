#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum = 0
    x = 1
    while x < len(my_list):
        if my_list[x] != my_list[x - 1]:
            sum += my_list[x]
        else:
            sum += 0
        x += 1
    sum += my_list[0]
    return sum
