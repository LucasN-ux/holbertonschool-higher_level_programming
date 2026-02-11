#!/usr/bin/python3
"""Script that returns a python object representing JSON format"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
