#!/usr/bin/python3
"""
Module that defines a Square
"""


class Square:
    """
    Class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Size of square

        :param self: reference to the current instance
        :param size: size(private)
        :param position: define the position
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Method who return the value of private size
        """
        return self.__size

    @property
    def position(self):
        """
        This method retrives the position of the suqare

        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Set the position of print square

        :param value: value input by user
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Area of square

        :param self: reference to the current instance
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return

        if int(self.__position[1]) > 0:
            for _ in range(int(self.__position[1])):
                print("")
        for _ in range(self.__size):
            print(" " * int(self.__position[0]), "#" * self.__size)
