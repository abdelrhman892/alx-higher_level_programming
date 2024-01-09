#!/usr/bin/python3
"""
    None
"""


class Student:
    """None"""

    def __init__(self, first_name, last_name, age):
        """None"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """None"""
        return self.__dict__
