#!/usr/bin/python3
"""
Square module - Contains the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Inherits from Rectangle.

    Attributes:
        Inherited from Rectangle:
            id (int): The id of the Square instance.
            width (int): The width of the Square instance.
            height (int): The height of the Square instance.
            x (int): The x-coordinate of the Square instance.
            y (int): The y-coordinate of the Square instance.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the Square.
            x (int): The x-coordinate of the Square. Default is 0.
            y (int): The y-coordinate of the Square. Default is 0.
            id (int): The id of the Square. Default is None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square instance.

        Returns:
            str: The formatted string representing the Square instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} \
- {self.width}"
