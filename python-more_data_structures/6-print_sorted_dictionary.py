#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    out = sorted(a_dictionary)
    for key in out:
        print("{}: {}".format(key, a_dictionary.get(key)))
