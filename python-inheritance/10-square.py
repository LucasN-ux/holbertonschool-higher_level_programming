#!/usr/bin/python3
"""ModuleDefines a BaseGeometry class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits class square"""
    def __init__(self, size):
        """init size of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area of size"""
        return self.__size * self.__size
