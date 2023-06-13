#!/usr/bin/python3
"""
This module implement the methode print_square.
"""


def print_square(size):
    """
    This methode prints a square with the character #.
    size - the size length of the square.
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)

