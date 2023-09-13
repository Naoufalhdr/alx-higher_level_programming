#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    result = 0

    for roman_char in roman_string:
        if roman_char in roman_dict.keys():
            result += roman_dict[roman_char]
        else:
            return 0
    return result
