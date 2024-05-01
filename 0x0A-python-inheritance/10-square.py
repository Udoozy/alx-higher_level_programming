#!/usr/bin/python3
"""Module for the 10 task"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """An inherited Class"""

    def __init__(self, size):
        """initialisation"""
        self.integer_validator("side", size)
        super().__init__(size, size)
        self.__size = size
