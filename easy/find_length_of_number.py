"""
Find length of a number.
Example:
    If given number is 0 then output should be 1 because this is a 1-digit number.
    If given number is 10 then output should be 2 because this is a 2-digit number.
    If given number is 100 then output should be 3 because this is a 3-digit number.
    If given number is 1234 then output should be 4 because this is a 4-digit number.
    If given number is of n digits then output should be n.
"""
from utils import input_util


def get_length_of_number(n):
    return len(str(n))


def main():
    number = input_util.get_positive_integer_from_input(attribute="integer")
    length_of_number = get_length_of_number(number)
    print(f"{number} is a {length_of_number}-digit number")


if __name__ == "__main__":
    main()