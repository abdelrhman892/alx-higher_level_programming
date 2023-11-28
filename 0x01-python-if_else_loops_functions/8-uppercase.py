#!/usr/bin/python3
def islower(c):
    if 96 <= ord(c) <= 122:
        return 1
def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) if not islower(c)
                            else ord(c) - 32), end="")
        print("")
