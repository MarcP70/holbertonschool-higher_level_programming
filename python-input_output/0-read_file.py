#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""


def read_file(filename=""):
    """This methode open, read and print the file.

    Args:
        filename (str): The name of the file.
    """
    with open('my_file_0.txt', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
