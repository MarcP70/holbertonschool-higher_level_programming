#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""
import json


def to_json_string(my_obj):
    """_summary_

    Args:
        my_obj (string): The object to convert on JSON representation.

    Returns:
        The JSON representation of an object (string).
    """
    return json.dumps(my_obj)
