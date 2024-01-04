#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Nothing"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Nothing"""
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Nothing"""
        return self.__width

    @width.setter
    def width(self, value):
        """Nothing"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Nothing"""
        return self.__height

    @height.setter
    def height(self, value):
        """Nothing"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Nothing"""
        return self.__height * self.__width

    def perimeter(self):
        """Nothing"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Nothing"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join([str(self.print_symbol)
                              * self.width] * self.height)

    def __repr__(self):
        """Nothing"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Nothing"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
