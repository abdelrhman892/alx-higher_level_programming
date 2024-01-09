#!/usr/bin/python3
"""Library for"""


class Student:
    """None"""

    def __init__(self, first_name, last_name, age):
        """None"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """None"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dick = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dick[key] = value
        return my_dick

    def reload_from_json(self, json):
        """None"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
