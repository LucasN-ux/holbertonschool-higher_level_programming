#!/usr/bin/python3
"""
A module that defines a CountedIterator class which
counts the number of items iterated.
"""


class CountedIterator:
    def __init__(self, iterable):
        """
        Initializes the CountedIterator with an iterable.
        """
        self._iterator = iter(iterable)
        self._count = 0

    def get_count(self):
        """
        Returns the number of items that have been iterated over.
        """
        return self._count

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next item from the iterator and increments the count.
        """
        item = next(self._iterator)
        self._count += 1
        return item
