"""
Maximum and Minimum: Find the maximum and minimum element in an array.
"""


def find_max_and_min_from_list(numbers):
    maximum, minimum = max(numbers), min(numbers)
    return maximum, minimum


def main():
    num_input = input("Enter numbers separated by spaces: ")
    num_list = num_input.split()
    num_list = [int(num) for num in num_list]
    maximum, minimum = find_max_and_min_from_list(num_list)
    print(f"From {num_list} , maximum = {maximum} and minimum = {minimum} ")


if __name__ == "__main__":
    main()