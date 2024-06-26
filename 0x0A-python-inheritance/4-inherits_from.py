#!/usr/bin/python3
"""Module for task 4"""


def inherits_from(obj, a_class):
    """return true if object is subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
