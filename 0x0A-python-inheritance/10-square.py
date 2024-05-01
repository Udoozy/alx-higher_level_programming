#!/usr/bin/python3
"""Module for the 10 task"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """An inherited Class"""

    def __init__(self, side):
        """initialisation"""
        self.integer_validator("side", side)
        self.__side = side
        super().__init__(side, side)

    def area(self):
        """Implemeting the Area"""
        return self.__side ** 2
