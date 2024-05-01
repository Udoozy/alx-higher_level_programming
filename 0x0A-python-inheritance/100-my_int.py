#!/usr/bin/python3
"""Module for Task 12"""


class MyInt(int):
    """Class inherited from int"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
