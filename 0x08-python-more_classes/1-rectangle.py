#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """clean"""
    def __init__(self, width=0, height=0):
        """clean"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """clean"""
        return self.width

    @width.setter
    def width(self, value):
        """clean"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value

    @property
    def height(self):
        """clean"""
        return self.height

    @height.setter
    def height(self, value):
        """clean"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.height = value
