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

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
