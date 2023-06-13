#!/usr/bin/python3
"""
This module implement the methode matrix_divided.
"""


def matrix_divided(matrix, div):
    """
    This methode divides all elements of a matrix.
    matrix - the list of lists of integers or floats
    div - the number to divide
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and rounding
    new_matrix = [[round(x/div, 2) for x in row] for row in matrix]

    return new_matrix
