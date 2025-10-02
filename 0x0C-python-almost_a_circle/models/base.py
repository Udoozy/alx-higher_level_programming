#!/usr/bin/python3
"""Module for the Base class"""
import json


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The Base class blueprint"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that conver to JSON"""
        if list_dictionaries is None or list_dictionaries is []:
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
        else:
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

    @classmethod
    def create(cls, **dictionary):
        """Method that return instance with attr set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """The classmethod that loads from a file"""
        try:
            Filemame = "{}.json".format(cls.__name__)
            with open(Filemame, 'r') as f:
                json_file = f.read()
                list_dicts = cls.from_json_string(json_file)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A class method that save file in CSV"""
        Filename = "{}.csv".format(cls.__name__)
        if list_objs == []:
            return []
        else:
            lists_dict = [obj.to_dictionary() for obj in list_objs]

            json_list = cls.to_json_string(lists_dict)

            with open(Filename, 'w') as f:
                f.write(json_list)

    @classmethod
    def load_from_file_csv(cls):
        """A class method that loads from csv"""
        Filename = "{}.csv".format(cls.__name__)
        try:
            with open(Filename, 'r') as f:
                json_file = f.read()

                lists_dict = cls.from_json_string(json_file)
                return [cls.create(**d) for d in lists_dict]
        except FileNotFoundError:
            return []
