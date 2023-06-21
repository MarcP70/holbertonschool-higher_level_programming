#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""
import json


def from_json_string(my_str):
    """This methode convert a JSON string representation
        to python data steructure.

    Args:
        my_str (JSON string): The JSON string representation.

    Returns:
        Python data structure: returns an object (Python data structure)
            represented by a JSON string.
    """
    return json.loads(my_str)
