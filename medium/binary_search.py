from utils import input_util


def binary_search(sorted_array, target):
    """
    Performs binary search on a sorted array to find the target value.

    Args:
        sorted_array: The sorted array to search in.
        target: The value to search for.

    Returns:
        The index of the target value in the array if found, otherwise -1.
    """

    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        current = sorted_array[mid]

        if current == target:
            return mid
        elif current > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def get_sorted_list_and_target():
    """
    Prompts user for a list of integers and a target element, ensuring they are sorted.

    Returns:
        A tuple containing the sorted list and the target element.
    """
    numbers = input_util.get_list_of_integers_from_input()
    numbers = sorted(numbers)  # Sort the input list
    target = input_util.get_positive_integer_from_input("target element to search:")
    return numbers, target


def main():
    sorted_array, target = get_sorted_list_and_target()
    index = binary_search(sorted_array, target)

    if index != -1:
        print(f"Target {target} found at index {index} in list {sorted_array}")
    else:
        print(f"Target {target} not found in the list {sorted_array}")


if __name__ == "__main__":
    main()
