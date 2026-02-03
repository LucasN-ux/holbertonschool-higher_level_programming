#!/usr/bin/python3
"""ModuleDefines a BaseGeometry class """


class BaseGeometry():
    """Represents a base geometry class"""
    def area(self):
        """Raises en exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
