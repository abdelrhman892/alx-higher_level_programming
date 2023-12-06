#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    new_list = my_list
    sum = 0
    x = 1
    while x < len(new_list):
        if new_list[x] != new_list[x - 1]:
            sum += new_list[x]
        else:
            sum += 0
        x += 1
    sum += new_list[0]
    return sum
