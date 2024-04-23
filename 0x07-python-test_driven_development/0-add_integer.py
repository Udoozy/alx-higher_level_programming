#!/usr/bin/python3
"""A module for adding two integers.
It takes two arguments.
Those argument can be float or integer.
It dosent support string.
"""


def add_integer(a, b=98):
    """User defined function that add two integers
    a,b(int): The first Argument
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
