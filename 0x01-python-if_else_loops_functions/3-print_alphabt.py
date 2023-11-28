#!/usr/bin/python3
num = 97
while num <= 122:
    if (num == 101) or (num == 113):
        num += 1
        continue
    print("{}".format(chr(num)), end="")
    num += 1
