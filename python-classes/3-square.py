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
        Docstring for __init__
        Size of square

        :param self: reference to the current instance
        :param size: size(private)
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Docstring for area
        Area of square

        :param self: reference to the current instance
        """
        return self.__size * self.__size
