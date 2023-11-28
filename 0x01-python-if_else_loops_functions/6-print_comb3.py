#!/usr/bin/python3
num = 1.0
deletedNum = 1.0
while int(num) <= 89:
    lastDigit = int(repr(int(num))[-1])
    if num < 89.0:
        if (lastDigit == 0) and (num > 9):
            deletedNum += 1.0
            num += deletedNum
        print("{:02}, ".format(int(num)), end="")
        num += 1
    else:
        if lastDigit == 9:
            deletedNum += 1.0
            num += deletedNum
        print("{:02}".format(int(num)))
        num += 1
