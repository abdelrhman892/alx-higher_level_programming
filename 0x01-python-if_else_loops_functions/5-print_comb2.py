#!/usr/bin/python3
num = 0.0
while int(num) <= 99:
    if num < 99.0:
        print("{:02}, ".format(int(num)), end="")
        num += 1
    else:
        print("{:02}".format(int(num)))
        num += 1
