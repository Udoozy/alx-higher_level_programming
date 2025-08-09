#!/usr/bin/python3
"""This is a program that print last name
and the first name of a user
"""


def say_my_name(first_name, last_name=""):
    """
    This is a function that handle the priting
    of the the first name and the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
