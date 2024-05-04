#!/usr/bin/python3
"""Module for appending to text"""


def append_write(filename="", text=""):
    """Funtion for append handling"""
    with open(filename, 'a') as my_file:
        return my_file.write(text)
