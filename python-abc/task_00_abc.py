#!/usr/bin/env python3
"""setting an Abstract class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class animal"""
    def __init__(self):
        pass

    @abstractmethod
    def sound(self):
        """sound method"""
        pass


class Dog(Animal):
    """Class Dog that inherits from Animal"""
    def sound(self):
        """sound method"""
        return "Bark"


class Cat(Animal):
    """Class Cat that inherits from Animal"""
    def sound(self):
        """sound method"""
        return "Meow"
