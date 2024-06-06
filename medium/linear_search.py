"""
Linear Search: Find the index of a target element in an array using linear search.
"""

from utils import  input_util


def linear_search(target, numbers):
    indices = []
    # Iterate through the list
    for i in range(len(numbers)):
        if numbers[i] == target: # Check each element if current element is equal to target
            indices.append(i) # Collect indices
    return indices


def main():
    numbers = input_util.get_list_of_integers_from_input()
    target = input_util.get_positive_integer_from_input("target whose indices are to be found")
    indices = linear_search(target, numbers)
    if indices:
        print(f"{target} is present at index: {indices} in given list  {numbers}")
    else:
        print(f"{target} is not present in the given list {numbers}")


if __name__ == "__main__":
    main()