#!/usr/bin/python3
""" A module that defines Fish and FlyingFish classes."""


class Fish():
    """
    A class representing a fish.
    """
    def swim(self):
        """
        Simulates the fish swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Simulates the fish's habitat.
        """
        print("The fish lives in water")


class Bird():
    """
    A class representing a bird.
    """
    def fly(self):
        """
        Simulates the bird flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Simulates the bird's habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, which inherits from both Fish and Bird.
    """
    def fly(self):
        """
        Simulates the flying fish flying.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Simulates the flying fish swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Simulates the flying fish's habitat.
        """
        print("The flying fish lives both in water and the sky!")
