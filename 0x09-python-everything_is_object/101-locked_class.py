#!/usr/bin/python3
"""Module that locks users from
   creating instances other than first_name
"""


class LockedClass:
    """Class that perform that uses __slots__
       to lock object instances
    """
    __slots__ = ["first_name"]
