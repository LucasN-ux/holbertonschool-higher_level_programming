#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file and prints it to stout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read())
