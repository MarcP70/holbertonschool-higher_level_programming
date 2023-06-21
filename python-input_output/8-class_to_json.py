#!/usr/bin/python3
"""
This module provides a function to convert an object to a JSON-serializable
    dictionary.
"""


def class_to_json(obj):
    """
    This methode convert an object to a JSON-serializable dictionary.

    Args:
        obj (object): The object to convert.

    Returns:
        dict: A dictionary representing the object's attributes.

    """
    return obj.__dict__
