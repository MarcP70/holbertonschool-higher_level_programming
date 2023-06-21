#!/usr/bin/python3
"""
This module provides functions for loading data from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    This methode load data from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: A dictionary containing the data from the JSON file.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If a JSON decoding error occurs.

    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        return json.loads(content)
