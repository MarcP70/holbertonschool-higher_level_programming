#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """This methode writes an Object to a text file,
        using a JSON representation.

    Args:
        my_obj (JSON representation): JSON representation of the object.
        filename (str): The name of the file to create.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
