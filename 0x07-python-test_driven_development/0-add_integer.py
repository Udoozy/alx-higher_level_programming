#!/usr/bin/python3
"""
It handles floats by converting to integers.
Function: add_integer(a, b=98)
Returns an integer result.
"""


def add_integer(a, b=98):
    """
    This is a module that adds two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
