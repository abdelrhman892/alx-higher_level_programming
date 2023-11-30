#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add, sub, mul, div
    a = 10
    b = 5
    c = 10
    d = 5
    print("{} + {} = {}".format(a, b, add(c, d)))
    print("{} - {} = {}".format(a, b, sub(c, d)))
    print("{} * {} = {}".format(a, b, mul(c, d)))
    print("{} / {} = {}".format(a, b, div(c, d)))
