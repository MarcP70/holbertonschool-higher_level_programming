#!/usr/bin/python3
"""
Module: geometry

This module provides classes for basic geometric shapes such as rectangles
    and squares.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.
        This method raises an Exception since it is not implemented in
            the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that the value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height