#!/usr/bin/python3
"""This module creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """This function reads json file and create obj"""
    with open(filename, 'r') as f:
        return json.load(f)
