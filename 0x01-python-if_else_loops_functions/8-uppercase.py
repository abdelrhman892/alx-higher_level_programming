#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 64 <= ord(i) <= 90:
            print("{}".format(i), end='')
        else:
            str = chr(ord(i) - 32)
            print("{}".format(str), end='')
