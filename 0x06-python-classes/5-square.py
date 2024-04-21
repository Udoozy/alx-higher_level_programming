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

    def my_print(self):
        """This Print square with # character"""
        for i in range(0, self.__size):
            [print("#", end="")for m in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
