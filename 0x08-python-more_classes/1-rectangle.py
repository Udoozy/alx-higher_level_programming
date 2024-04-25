#!/usr/bin/python3
"""Full definition of recangle class"""


class Rectangle:
    """Defined class"""

    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width_setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height_setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
