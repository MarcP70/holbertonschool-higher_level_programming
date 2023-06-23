#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle
    up to a specified number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
