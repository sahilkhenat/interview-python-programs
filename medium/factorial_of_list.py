"""
Find Factorial of Each Number in a List: Calculate the factorial of each number in a list.
"""

from utils import input_util


def factorial_of_list(numbers):
    factorials = [factorial(i) for i in numbers]
    return factorials


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    list_of_numbers = input_util.get_list_of_positive_integers_from_input()
    print(f"List of given numbers: {list_of_numbers}")
    list_of_factorials = factorial_of_list(list_of_numbers)
    print(f"List of respective factorials: {list_of_factorials}")


if __name__ == "__main__":
    main()
