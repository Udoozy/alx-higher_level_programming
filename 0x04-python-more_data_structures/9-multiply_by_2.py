#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary:
        for i, j in a_dictionary.items():
            new_dict.update({i: j * 2})
    return new_dict
