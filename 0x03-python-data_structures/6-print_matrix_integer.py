#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in matrix:
            for elements in row:
                print("{:d}".format(elements), end=" ")
            print()
