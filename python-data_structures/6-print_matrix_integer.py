#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
