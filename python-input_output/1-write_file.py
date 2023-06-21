#!/usr/bin/python3
"""This module manipulate Input/Output with a file.
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        nb_char_written = f.write(text)
        return nb_char_written
