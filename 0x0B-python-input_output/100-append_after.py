#!/usr/bin/python3
"""Module That searched a string"""


def append_after(filename="", search_string="", new_string=""):
    """FUnction that perform search and add to the buttom"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
