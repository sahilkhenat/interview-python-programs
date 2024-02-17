"""
Program to calculate factorial of given number.
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    number = input("Enter a number for which you want to find factorial:")
    print(factorial(number))


if __name__ == "__main__":
    main()
