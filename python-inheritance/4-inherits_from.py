#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ object is an instance of an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    return False
