#!/usr/bin/python3
"""
Module that defines a Square
"""


class Square:
    """
    Class that defines a square
    """
    def __init__(self, size=0):
        """
        Function that define a size
        Docstring for __init__

        :param self: refere to function
        :param size: size(private)
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("syze must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
