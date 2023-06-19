#!/usr/bin/python3
"""
This module contains one function for a class of an object.
"""


def is_same_class(obj, a_class):
    """
    This methode returns True if the object is exactly an instance
        of the specified class ; otherwise False.

    Args:
        obj: The instance of object to check.
        a_class: The specified class.

    Returns:
        boolean: True or false.
    """

    if type(obj) is a_class:
        return True
    return False
