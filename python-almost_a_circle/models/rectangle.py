#!/usr/bin/python3
"""
Rectangle module - Contains the Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The ID of the rectangle.

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            ValueError: If the width value is not positive.

        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            ValueError: If the height value is not positive.

        """
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            ValueError: If the x-coordinate value is negative.

        """
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            ValueError: If the y-coordinate value is negative.

        """
        self.__y = value
