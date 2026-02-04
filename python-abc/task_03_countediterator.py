#!/usr/bin/env python3
"""CountedIterator class that tracks iteration count"""


class CounterIterator:
    """Count how many items were iterated"""

    def __init__(self, iterable):
        """body method"""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """iter method"""
        return self

    def __next__(self):
        """next method"""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items returned so far."""
        return self.count
