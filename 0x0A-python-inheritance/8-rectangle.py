#!/usr/bin/python3
"""Module for the 8 task"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """An inherited Class"""

    def __init__(self, width, height):
        """initialisation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
