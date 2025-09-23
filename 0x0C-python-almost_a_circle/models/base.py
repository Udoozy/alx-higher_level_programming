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

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that save_Json to a file"""
        Filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            lists_dict = []
        lists_dict = [obj.to_dictionary() for obj in list_objs]

        json_file = cls.to_json_string(lists_dict)

        with open(Filename, 'w') as f:
            f.write(json_file)

    @staticmethod
    def from_json_string(json_string):
        """A static method that return Json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
