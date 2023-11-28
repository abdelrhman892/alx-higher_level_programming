#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = int(repr(int(number))[-1])
    print("{}".format(lastDigit), end="")
    return lastDigit
