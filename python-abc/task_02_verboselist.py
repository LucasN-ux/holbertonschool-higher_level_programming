#!/usr/bin/python3
"""setting an Abstract class"""


class VerboseList(list):
    """class named VerboseList that extends the Python list class"""
    def append(self, item):
        """append method"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """extend method"""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """remove method"""
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=-1):
        """pop method"""
        item = super().pop(item)
        print("Popped [{}] from the list.".format(item))
