#!/usr/bin/python3
"""Module for the Base class"""
import json


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that conver to JSON"""
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        else:
            json_format = json.dumps(list_dictionaries)
            return json_format
