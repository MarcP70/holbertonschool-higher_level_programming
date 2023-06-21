#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""


def read_file(filename=""):
    """This methode open, read and print the file.

    Args:
        filename (str): The name of the file.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
