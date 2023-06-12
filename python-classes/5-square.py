#!/usr/bin/python3
"""
This module includes a class Square that defines a square.
"""


class Square:
    """
    This class represents a square and provides methods for square operations.
    """

    def __init__(self, size=0):
        """
        This methode initializes a new instance of the Square class.
        Parameters:
        - self: The Square instance being initialized.
        - size: The Size.
        """
        self.__size = size

    @property
    def size(self):
        """Get"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        This methode returns the current square area.
        Parameters:
        - self: The Square instance.
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
