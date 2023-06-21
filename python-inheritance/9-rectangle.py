#!/usr/bin/python3
"""
Module: geometry

This module provides classes for basic geometric shapes such as rectangles
    and squares.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
