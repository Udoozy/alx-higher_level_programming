#!/usr/bin/python3
"""Module to check for attribute"""


def add_attribute(obj, name, value):
    """Addss attribute if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    
    setattr(obj, name, value)
