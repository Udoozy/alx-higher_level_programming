#!/usr/bin/python3
"""Module for task 7"""


class BaseGeometry:
    """The Clas defined"""

    def area(self):
        """Unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """An integer validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
