"""
Find Duplicate Number: Find the duplicate numbers in an array of integers from 1 to n.
"""

from utils import input_util


def find_duplicates_in_list(numbers):
    seen = set()
    duplicates = set()

    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


def main():
    numbers = input_util.get_list_of_integers_from_input()
    duplicate_numbers = find_duplicates_in_list(numbers)
    print(f"Duplicate numbers in {numbers} are: {duplicate_numbers}")


if __name__ == "__main__":
    main()
