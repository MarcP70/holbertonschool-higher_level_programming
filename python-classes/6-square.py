#!/usr/bin/python3
"""
This module includes a class Square that defines a square.
"""


class Square:
    """
    This class represents a square and provides methods for square operations.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This methode initializes a new instance of the Square class.
        Parameters:
        - self: The Square instance being initialized.
        - size: The Size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def size(self):
        """Get"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0 or type(value) is not tuple\
                or len(value) != 2 or type(value[0]) is not int\
                or type(value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
