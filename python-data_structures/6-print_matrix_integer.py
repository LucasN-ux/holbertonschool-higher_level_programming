#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            i = line[i]
            if i != len(line):
                print("{:d}".format(i), end=(" "))
            else:
                print("{:d}".format(i), end="")
        print()
