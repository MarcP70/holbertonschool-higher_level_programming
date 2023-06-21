#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""


def write_file(filename="", text=""):
    """This methode write into a file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write.

    Returns:
        int: The number of char written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        nb_char_written = f.write(text)
        return nb_char_written
