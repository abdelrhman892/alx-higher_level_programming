#!/usr/bin/python3
"""anything"""


class Square:
    """anything"""
    def __init__(self, size=0, position=(0, 0)):
        """constractur"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.position = position

    @property
    def size(self):
        """to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """to get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """to set position"""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(i, int) for i in value)
                or any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """to calc area"""
        return self.__size ** 2

    def my_print(self):
        """to display the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for z in range(self.__position[0]):
                    print('_', end='')
                for x in range(self.__size):
                    print('#', end='')
                print()
