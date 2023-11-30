#!/usr/bin/python3

_input = input()
argv = _input.split()
arguments = len(argv)
num = 1
if arguments != 0:
    print("{} arguments:".format(arguments))
    for i in argv:
        print("{}: {}".format(num, i))
        num += 1
else:
    print("0 arguments.")
