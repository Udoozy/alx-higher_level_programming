#!/usr/bin/python3
"""Check for instance"""


def is_same_class(obj, a_class):
    """Return True if obj is an instance of a_class, False"""
    return type(obj) is a_class
