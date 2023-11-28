#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 64 and ord(i) <= 90:
            print(i, end='')
        else:
            str = chr(ord(i) - 32)
            print(str, end='')
