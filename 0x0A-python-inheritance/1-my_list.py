#!/usr/bin/python3
"""Inheritance"""


class MyList(list):
    """List subclass"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
