#!/usr/bin/python3
from models.base import Base

"""
    This class will be the Rectangle
    to clac all things about Rectangle
"""


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if type(x) not in [int]:
            raise TypeError("x must be an integer")
        if type(y) not in [int]:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) not in [int]:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.height

    def display(self):
        for i in range(self.y):
            print()
        for L in range(self.height):
            for c in range(self.x):
                print(" ", end='')
            for W in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        attribute_mapping = {'id': self.id, 'height': self.height,
                             'width': self.width, 'x': self.x, 'y': self.y}

        for key, value in kwargs.items():
            if key in attribute_mapping:
                setattr(self, key, value)

        for arg, key in enumerate(('id', 'width', 'height', 'x', 'y')):
            if arg < len(args):
                setattr(self, key, args[arg])

    def to_dictionary(self):
        return{
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
