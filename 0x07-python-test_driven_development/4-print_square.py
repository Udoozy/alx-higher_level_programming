#!/usr/bin/python3
"""
The function print # a number of size
and display the result to the output
"""


def print_square(size):
    """
    This function takes a size Arguments
    and check if it meets the condition
    and evaluate accordiingly
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    n = 0
    while n < size:
        for i in range(size):
            print('#', end="")
        print("")
        n = n + 1


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/4-print_square.txt")
