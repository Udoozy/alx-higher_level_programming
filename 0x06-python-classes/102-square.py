#!/usr/bin/python3
"""Module to compute size of square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """initializing a new square size
        Args:
            size(int): Size of the Square
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size and value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the actual area vlaue"""
        return (self.__size * self.__size)

    def __eq__(self, value):
        """This check for equality"""
        if isinstance(value, Square):
            return self.area() == value.area()
        return NotImplemented

    def __ne__(self, value):
        """This check for not equal to"""
        if isinstance(value, Square):
            return self.area() != value.area()
        return NotImplemented

    def __gt__(self, value):
        """This check for greater than"""
        if isinstance(value, Square):
            return self.area() > value.area()
        return NotImplemented

    def __ge__(self, value):
        """This the for greater than or equal to"""
        if isinstance(value, Square):
            return self.area() >= value.area()
        return NotImplemented

    def __lt__(self, value):
        """This checks for less than"""
        if isinstance(value, Square):
            return self.area() < value.area()
        return NotImplemented

    def __le__(self, value):
        """This checks for less than or equal to"""
        if isinstance(value, Square):
            return self.area() <= value.area()
        return NotImplemented
