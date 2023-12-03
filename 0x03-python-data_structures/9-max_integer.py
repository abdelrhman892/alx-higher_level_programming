#!/usr/bin/python3
def max_integer(my_list=[]):
    are_all_ints = all(isinstance(x, int) for x in my_list)

    if are_all_ints:
        if len(my_list) == 0:
            return None
        else:
            my_list.sort()
            return my_list[-1]
    else:
        return None
