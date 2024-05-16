"""Check Armstrong Number: Check if a given number is an Armstrong number.
What is Armstrong number :
An Armstrong number, also known as a narcissistic number or a plenary number, is a number that is equal to the sum of its own digits raised to the power of the number of digits.

In other words, let's say we have an n-digit number. If we raise each digit of the number to the power of n, and then sum these values, if the result is equal to the original number, then that number is called an Armstrong number.

For example, 153 is an Armstrong number because:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

Similarly, 407 is an Armstrong number because:
4^3 + 0^3 + 7^3 = 64 + 0 + 343 = 407

However, numbers like 123 are not Armstrong numbers because:
1^3 + 2^3 + 3^3 = 1 + 8 + 27 ≠ 123
"""
from utils import input_util
from easy import find_length_of_number


def is_armstrong_number(number):
    length = find_length_of_number.get_length_of_number(number)
    sum_of_powers = 0
    num = number
    for i in range(length):
        remainder = num % 10
        sum_of_powers += remainder ** 3
        num = num // 10
    if sum_of_powers == number:
        return True
    else:
        return False


def main():
    number = input_util.get_positive_integer_from_input("number")
    if is_armstrong_number(number):
        print(f"{number} is an armstrong number")
    else:
        print(f"{number} is NOT an armstrong number")


if __name__ == "__main__":
    main()
