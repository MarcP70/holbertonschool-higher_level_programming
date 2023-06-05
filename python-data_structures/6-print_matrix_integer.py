#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            i = 1
            for num in row:
                if i != len(row):
                    print("{:d}".format(num), end=" ")
                else:
                    print("{:d}".format(num), end="")
                i += 1
            print()
