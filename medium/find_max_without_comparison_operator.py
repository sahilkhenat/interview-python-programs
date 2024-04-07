"""
Find Maximum of Two Numbers: Find the maximum of two numbers without using comparison operators.
"""
from utils import input_util


def find_max_without_comparison_operator(a, b):
    # Calculate the difference between a and b
    diff = a - b
    # Calculate the sign of the difference (1 if a >= b, 0 otherwise)
    sign = (diff >> 31) & 1
    # Use conditional expression to select the maximum value
    return a * (1 - sign) + b * sign


def main():
    n1 = input_util.get_positive_integer_from_input("Number")
    n2 = input_util.get_positive_integer_from_input("Number")
    maximum = find_max_without_comparison_operator(n1, n2)
    print(f"Maximum from {n1} and {n2} is :{maximum}")


if __name__ == "__main__":
    main()
