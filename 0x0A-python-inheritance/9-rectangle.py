#!/usr/bin/python3
"""Module for the 9 task"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """An inherited Class"""

    def __init__(self, width, height):
        """initialisation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Implemeting the Area"""
        return self.__width * self.__height

    def __str__(self):
        """This return the format described"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
