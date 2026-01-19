#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    while i >= my_list[0]:
        print("{:d}".format(i))
        i = i - 1
