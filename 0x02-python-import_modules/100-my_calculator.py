#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sIgn = sys.argv[2]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sIgn == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sIgn == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sIgn == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sIgn == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
