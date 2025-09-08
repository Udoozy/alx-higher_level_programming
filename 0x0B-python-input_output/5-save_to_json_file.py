#!/usr/bin/python3
"""Module that writes object file into a json file"""
import json


def save_to_json_file(my_obj, filename):
    """The write function for json"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
