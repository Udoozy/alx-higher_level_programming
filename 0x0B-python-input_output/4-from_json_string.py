#!/usr/bin/python3
"""This module takes the json and return the python fmt
"""
import json


def from_json_string(my_str):
    """The function that perfort the deserialization"""
    return json.loads(my_str)
