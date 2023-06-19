#!/usr/bin/python3
"""
This module contains one function for checking if the object is an instance
    of a class.
"""


def is_kind_of_class(obj, a_class):
    """
    This methode returns True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the specified class ;
        otherwise False

    Args:
        obj: The instance of object to check.
        a_class: The specified class.

    Returns:
        boolean: True or false.
    """

    return isinstance(obj, a_class)
