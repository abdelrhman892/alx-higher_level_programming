#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """A class to represent rectangles."""

    number_of_instances = 0
    default_print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with the given width and height."""
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join([str(self.default_print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        return f"Rectangle(width={self.__width}, height={self.__height})"

    def __del__(self):
        """Destructor for the Rectangle class."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

