#!/usr/bin/python3
"""script than contain function"""


def is_kind_of_class(obj, a_class):
    """ object is an instance of an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
