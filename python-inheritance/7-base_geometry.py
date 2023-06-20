#!/usr/bin/python3
"""This module has a class.

Raises:
    Exception: area() is not implemented.
    TypeError: <name> must be an integer.
    ValueError: <name> must be greater than 0.
"""


class BaseGeometry:
    """This class two methodes.

    Raises:
        Exception: area() is not implemented.
        TypeError: <name> must be an integer.
        ValueError: <name> must be greater than 0.
    """

    def area(self):
        """Public instance method.

        Raises:
            Exception: area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method.

        Args:
            name (string): The name.
            value (int): The value.

        Raises:
            TypeError: <name> must be an integer.
            ValueError: <name> must be greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
