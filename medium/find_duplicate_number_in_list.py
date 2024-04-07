"""
Find Duplicate Number: Find the duplicate number in an array of integers from 1 to n.
"""
from utils import input_util
from medium import calculate_occurrences_of_each_item_in_list as co


def find_duplicate_number(numbers):
    occurrences = co.calculate_occurrences(numbers)
    duplicates = [item for item, count in occurrences.items() if count > 1]
    return duplicates


def main():
    numbers = input_util.get_list_of_integers_from_input()
    duplicates = find_duplicate_number(numbers)
    print(f"Duplicates in {numbers} are as follows :- {duplicates}")


if __name__ == "__main__":
    main()
