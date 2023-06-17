#!/usr/bin/python3
"""
This module implement the methode text_indentation.
"""


def text_indentation(text):
    """
    This methode prints a text with 2 new lines after each of
        these characters: '.', '?' and ':'.
    text - the text to indente.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end='')
