#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    if not roman_string:
        return 0
    for char in roman_string:
        value = roman_num[char]
        total += roman_num[char]
    return total
