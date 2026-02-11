#!/usr/bin/python3
"""Script that prints a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
