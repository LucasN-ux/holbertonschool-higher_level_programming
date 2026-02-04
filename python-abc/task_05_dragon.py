#!/usr/bin/python3
"""
Module defining the Dragon class with swimming, flying,
and roaring capabilities.
"""


class SwimMixin:
    """
    Mixin class to add swimming capability.
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class to add flying capability.
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon with swimming, flying,
    and roaring capabilities.
    """
    def roar(self):
        print("The dragon roars!")
