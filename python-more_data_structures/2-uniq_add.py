#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    copy = set(my_list)
    for i in copy:
        result += i
    return result
