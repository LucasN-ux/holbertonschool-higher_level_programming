#!/usr/bin/python3
"""script than contain function"""


def is_same_class(obj, a_class):
    """ object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    return False
