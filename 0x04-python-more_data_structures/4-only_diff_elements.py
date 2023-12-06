#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list1 = list(set_1)
    my_list2 = list(set_2)
    my_list3 = []
    my_list4 = []
    target = ""
    for i in my_list2:
        for x in my_list1:
            if i == x:
                target = i

    my_list3.append(my_list1)
    my_list3.append(my_list2)
    for i in my_list3:
        for j in i:
            my_list4.append(j)
    my_list4.remove(target)
    my_list4.remove(target)
    my_list4 = set(my_list4)
    return my_list4
