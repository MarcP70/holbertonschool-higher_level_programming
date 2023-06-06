#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return
    multiplied_dict = {}
    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2
    return multiplied_dict
