#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list1 = list(set_1)
    my_list2 = list(set_2)
    my_list3 = []
    for i in my_list1:
        for x in my_list2:
            if i == x:
                my_list3.append(i)
    my_list3 = set(my_list3)
    return my_list3
