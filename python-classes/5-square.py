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
        Size of square

        :param self: reference to the current instance
        :param size: size(private)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Area of square

        :param self: reference to the current instance
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Method who return the value of private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter to the user change the value of size

        :param value: size of square input by user
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        line = 0
        if self.__size == 0:
            print()
        if self.__size > 0:
            for i in range(self.__size ** 2):
                line += 1
                print("#", end="")
                if line == self.__size:
                    print()
                    line = 0
