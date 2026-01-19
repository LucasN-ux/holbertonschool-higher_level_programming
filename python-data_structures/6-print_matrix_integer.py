#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in line:
            print("{:d}".format(i), end=" ")
        print()
