#!/usr/bin/python3
"""
Module thaan define a rectangle
"""


class Rectangle:
    """
    Class than define a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Init method

        :param width: Width of rectangle
        :param height: Height of rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Method who return the private width
        """
        return self.__width

    @property
    def height(self):
        """
        Method who return the private height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter to change value of width

        :param value: width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter to change value of height

        :param value: height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            perim = 0
        else:
            perim = 2 * (self.__width + self.__height)
        return (perim)

    def __str__(self):
        """
        Print a rectangle
        """
        my_str = ""
        if self.__width != 0 and self.__height != 0:
            for _ in range(self.__height):
                my_str += self.__width * "#"
                if _ != self.__height - 1:
                    my_str += "\n"
        return my_str

    def __repr__(self):
        """
        Reproduce object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
