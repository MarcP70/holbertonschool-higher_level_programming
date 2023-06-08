#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                    'D': 500, 'M': 1000}
    result = 0
    previous_value = 0

    for char in reversed(roman_string):
        if roman_values[char] >= previous_value:
            result += roman_values[char]
        else:
            result -= roman_values[char]
        previous_value = roman_values[char]

    return result
