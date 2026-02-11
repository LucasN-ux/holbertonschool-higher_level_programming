#!/usr/bin/python3
"""Script that saves a object in a file in JSON format"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return json.dump(my_obj, f)
