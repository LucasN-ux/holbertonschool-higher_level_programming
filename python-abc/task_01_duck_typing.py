#!/usr/bin/env python3
"""setting an Abstract class"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract Shape class"""

    @abstractmethod
    def area(self):
        """Area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Permimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Define a radius of the circle"""
        self.__radius = radius

    def area(self):
        """Area of the shape"""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Permimeter of the shape"""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Define a width and height of the rectangle"""
        self.__width = width
        self.__height = height

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Permimeter of the rectangle"""
        return 2 * (self.__width + self.__height)


def shape_info(arg):
    print("Area: {}".format(arg.area()))
    print("Perimeter: {}".format(arg.perimeter()))
