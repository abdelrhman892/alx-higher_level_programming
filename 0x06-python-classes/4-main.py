#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.getSize()))

my_square.setSize(3)
print("Area: {} for size: {}".format(my_square.area(), my_square.getSize()))

try:
    my_square.setSize("5 feet")
    print("Area: {} for size: {}".format(my_square.area(), my_square.getSize()))
except Exception as e:
    print(e)
