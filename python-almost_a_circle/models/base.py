#!/usr/bin/python3
"""
This module provides a base class for objects with an ID.
"""


class Base:
    """
    A base class representing an object with an ID.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int): The ID of the object. If not provided,
                a new ID is assigned.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
