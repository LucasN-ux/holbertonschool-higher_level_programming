#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []

    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i ** 2)
        new.append(new_row)
    return new
