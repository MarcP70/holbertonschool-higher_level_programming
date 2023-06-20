#!/usr/bin/python3
"""
This module contains one function for checking if the object is an instance
    or a subinstance of a class.
"""


def inherits_from(obj, a_class):
    """
    This methode returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class ;
        otherwise False.

    Args:
        obj: The instance of object to check.
        a_class: The specified class.

    Returns:
        boolean: True or false.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
