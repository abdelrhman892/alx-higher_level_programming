#!/usr/bin/python3
from models.rectangle import Rectangle

"""
    This class will be the Square
    to clac all things about Square
"""


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{Square.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        # for key, value in kwargs.items():
        #     if key == 'id':
        #         self.id = value
        #     if key == 'size':
        #         self.size = value
        #     if key == 'x':
        #         self.x = value
        #     if key == 'y':
        #         self.y = value
        # for arg in range(len(args)):
        #     if arg == 0:
        #         self.id = args[arg]
        #     if arg == 1:
        #         self.size = args[arg]
        #     if arg == 2:
        #         self.x = args[arg]
        #     if arg == 3:
        #         self.y = args[arg]
        attribute_mapping = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

        for key, value in kwargs.items():
            if key in attribute_mapping:
                setattr(self, key, value)

        for arg, key in enumerate(('id', 'size', 'x', 'y')):
            if arg < len(args):
                setattr(self, key, args[arg])
