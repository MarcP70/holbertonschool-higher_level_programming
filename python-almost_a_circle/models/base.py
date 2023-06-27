#!/usr/bin/python3
"""
This module provides a base class for objects with an ID.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by the JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries
                in JSON format.

        Returns:
            list: The list of dictionaries represented by the JSON string.
                If the JSON string is None or empty,
                    an empty list is returned.

        """
        json_list = []
        if json_string is None or len(json_string) == 0:
            return json_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set based
            on the provided dictionary.

        Args:
            **dictionary: Double pointer to a dictionary containing
                the attributes of the instance.

        Returns:
            Base: An instance of the class with the attributes set
                based on the provided dictionary.

        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance

        # Apply the real attribute values using update method
        dummy_instance.update(**dictionary)
        return dummy_instance
