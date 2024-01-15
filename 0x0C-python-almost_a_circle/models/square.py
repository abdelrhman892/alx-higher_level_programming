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
        return (f"[{Square.__name__}] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attribute_mapping = {'id': self.id, 'size': self.size,
                             'x': self.x, 'y': self.y}

        for key, value in kwargs.items():
            if key in attribute_mapping:
                setattr(self, key, value)

        for arg, key in enumerate(('id', 'size', 'x', 'y')):
            if arg < len(args):
                setattr(self, key, args[arg])

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
