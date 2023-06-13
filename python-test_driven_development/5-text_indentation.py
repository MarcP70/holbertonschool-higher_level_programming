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

    new_text = ""
    i = 0
    while i < len(text):
        if text[i] in ('.', '?', ':'):
            new_text += text[i]
            if i != len(text) -1:
                new_text += '\n\n'
            i += 1
        else:
            new_text += text[i]
        i += 1
    print(new_text, end='')
