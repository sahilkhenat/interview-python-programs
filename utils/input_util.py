"""
This file contains reusable code, helper functions related to accepting input from user in different formats and types.
"""


def get_positive_integer_from_input(attribute):
    integer_input = input(f"Enter a {attribute}(integer value):")
    return int(integer_input)


def get_string_from_input(attribute):
    string_input = input(f"Enter a {attribute}(string value):")
    return string_input


def get_list_of_positive_integers_from_input():
    try:
        input_numbers = input("Enter a list of positive numbers separated by spaces: ")
        numbers_list = input_numbers.split()
        positive_numbers = [int(num) for num in numbers_list]

        for num in positive_numbers:
            if num < 1:
                raise ValueError(f"{num} is a non-positive number in the list: {positive_numbers}")

        return positive_numbers

    except ValueError as e:
        print(f"Error: {e}")
        return None


def get_list_of_integers_from_input():
    input_numbers = input("Enter a list of integer numbers separated by spaces: ")
    numbers_list = input_numbers.split()
    numbers = [int(num) for num in numbers_list]
    return numbers


def get_list_of_floats_from_input():
    input_numbers = input("Enter a list of float numbers separated by spaces: ")
    numbers_list = input_numbers.split()
    numbers_float_list = [float(i) for i in numbers_list]
    return numbers_float_list


def get_list_of_strings_from_input():
    input_numbers = input("Enter a list of strings separated by spaces: ")
    strings_list = input_numbers.split()
    return strings_list
