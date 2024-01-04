#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """nothing"""

    def __init__(self, width=0, height=0):
        """nothing"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """nothing"""
        return self.__width

    @width.setter
    def width(self, value):
        """nothing"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """nothing"""
        return self.__height

    @height.setter
    def height(self, value):
        """nothing"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """nothing"""
        return self.__height * self.__width

    def perimeter(self):
        """nothing"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """nothing"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """nothing"""
        return f"Rectangle{eval('(self.width, self.height)')}"

    def __del__(self):
        """nothing"""
        print('Bye rectangle...')
    
