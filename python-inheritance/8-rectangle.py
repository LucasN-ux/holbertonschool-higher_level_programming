#!/usr/bin/python3
"""ModuleDefines a BaseGeometry class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits who define a rectangle"""
    def __init__(self, width, height):
        """init width and height of the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
