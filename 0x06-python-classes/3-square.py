#!/usr/bin/python3
"""The Square module"""


class Square:
    """The square class"""
    def __init__(self, size=0):
        """A new size initialized.
        Args:
        size(int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def def area(self):
        """The definition of area function"""
        return (self.__size * self.__size)
