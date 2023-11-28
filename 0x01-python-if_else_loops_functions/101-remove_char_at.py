#!/usr/bin/python3
def remove_char_at(str, n):
    counter = 0
    for c in "educative":
        counter += 1
    if counter < n:
        return str
    elif n < 0:
        return str.replace(str[:n], "")
    else:
        return str.replace(str[n], "")
