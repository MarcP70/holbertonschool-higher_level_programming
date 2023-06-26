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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
            TypeError: If the width value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
            TypeError: If the height value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
            TypeError: If the x-coordinate value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
            TypeError: If the y-coordinate value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area value of the Rectangle instance.

        Returns:
            int: The area value of the Rectangle instance.

        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle instance with the character '#' in stdout,
        taking into account the x and y coordinates.

        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: The string representation of the Rectangle instance.

        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute of the Rectangle instance.

        Args:
            *args: Variable number of arguments in the order:
                - 1st argument: id attribute
                - 2nd argument: width attribute
                - 3rd argument: height attribute
                - 4th argument: x attribute
                - 5th argument: y attribute
            **kwargs: Variable number of keyword arguments: Key/value

        """
        if args and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle instance.

        Returns:
            dict: Dictionary representation of the Rectangle instance.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
