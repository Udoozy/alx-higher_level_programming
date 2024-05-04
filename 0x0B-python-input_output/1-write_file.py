#!/usr/bin/python3
"""Writing module"""


def write_file(filename="", text=""):
    """Write function"""
    with open(filename, 'w') as my_file:
        return my_file.write(text)
