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
        if self.x >= 2:
            for i in range(self.x):
                print()
        for L in range(self.height):
            for c in range(self.y):
                print(" ", end='')
            for W in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            if key == 'height':
                self.height = value
            if key == 'width':
                self.width = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value
        for arg in range(len(args)):
            if arg == 0:
                self.id = args[arg]
            if arg == 1:
                self.__width = args[arg]
            if arg == 2:
                self.__height = args[arg]
            if arg == 3:
                self.__x = args[arg]
            if arg == 4:
                self.__y = args[arg]
