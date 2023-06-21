#!/usr/bin/python3
"""
Module: geometry

This module provides classes for basic geometric shapes such as rectangles
    and squares.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square shape, which is a special case of a rectangle.
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
