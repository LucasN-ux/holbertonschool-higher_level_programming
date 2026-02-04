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
        """Perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Define a radius of the circle"""
        self.radius = radius

    def area(self):
        """Area of the shape"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter of the shape"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Define a width and height of the rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(arg):
    print("Area: {}".format(arg.area()))
    print("Perimeter: {}".format(arg.perimeter()))
