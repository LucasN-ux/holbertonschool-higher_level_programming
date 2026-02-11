#!/usr/bin/python3
"""Script that returns the dictionary description"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    my_obj = obj.__dict__
    return my_obj
