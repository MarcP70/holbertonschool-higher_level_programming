#!/usr/bin/python3
"""This module has a class.

Raises:
    Exception: area() is not implemented.
    TypeError: <name> must be an integer.
    ValueError: <name> must be greater than 0.
"""


class BaseGeometry:
    """This class define bases of geometry.

    Raises:
        Exception: area() is not implemented.
        TypeError: <name> must be an integer.
        ValueError: <name> must be greater than 0.
    """

    pass

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


class Rectangle(BaseGeometry):
    """This class define a rectangle.

    Args:
        BaseGeometry (class): define bases of geometry.
    """

    def __init__(self, width, height):
        """This methode initialize the instance of object rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This methode reurn the area of the rectangle.

        Returns:
            _type_: _description_
        """

        return self.__width * self.__height

    def __str__(self):
        """This methode return the rectangle description.

        Returns:
            string: [Rectangle] <width>/<height>
        """
        
        return f"[Rectangle] {self.__width}/{self.__height}"

