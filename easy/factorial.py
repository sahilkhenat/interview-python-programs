"""
Program to calculate factorial of given number.
"""
from utils import input_util


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    number = input_util.get_positive_integer_from_input("number")
    print(f"{number}! is equal to {factorial(number)}")


if __name__ == "__main__":
    main()
