"""
Calculate occurrences of each item in a given list . Return a dictionary that has key = item , value = number of occurrences of the item in given list
"""
from utils import input_util


def calculate_occurrences(item_list):
    occurrences = {}
    for item in item_list:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences


def main():
    numbers = input_util.get_list_of_integers_from_input()
    letters = input_util.get_list_of_strings_from_input()
    counts_of_numbers = calculate_occurrences(numbers)
    counts_of_strings = calculate_occurrences(letters)
    print("Count of numbers entered is as follows:", counts_of_numbers)
    print("Count of strings entered is as follows:", counts_of_strings)


if __name__ == "__main__":
    main()