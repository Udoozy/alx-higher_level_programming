#!/usr/bin/python3
import doctest
"""A module for adding two integers.
It takes two arguments.
Those argument can be float or integer.
It dosent support string.
"""


def add_integer(a, b=98):
    """User defined function that add two integers
    a,b(int): The first Argument
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
