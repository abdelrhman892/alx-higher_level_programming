#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    last_string = ""

    for i in range(len(my_string)):
        if my_string[i] != "c":
            new_string += my_string[i]

    for x in range(len(new_string)):
        if new_string[x] != "C":
            last_string += new_string[x]

    return last_string
