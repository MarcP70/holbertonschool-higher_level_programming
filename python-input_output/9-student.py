#!/usr/bin/python3
"""
This module provides a Student class representing a student
    and related methods.
"""


class Student:
    """
    A class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Convert the Student object to a JSON-serializable dictionary.

        Returns:
            dict: A dictionary representing the Student object.

        """
        json_data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_data
