#!/usr/bin/python3
"""Module for class serailization"""


def class_to_json(obj):
    """Function thazt perforn the serialization"""
    return obj.__dict__
