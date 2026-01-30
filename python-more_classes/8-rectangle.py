#!/usr/bin/python3
"""
Module thaan define a rectangle
"""


class Rectangle:
    """
    Class than define a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        rectangle_area = self.__height * self.__width
        return rectangle_area

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
                my_str += self.__width * str(self.print_symbol)
                if _ != self.__height - 1:
                    my_str += "\n"
        return my_str

    def __repr__(self):
        """
        Reproduce object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        delete rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        rectangle_area1 = rect_1._Rectangle__height * rect_1._Rectangle__width
        rectangle_area2 = rect_2._Rectangle__height * rect_2._Rectangle__width

        if rectangle_area1 >= rectangle_area2:
            return rect_1
