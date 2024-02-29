"""Write a program to check if given number is prime or not,"""
import math


def check_prime_or_not(number):
    square_root = round(math.sqrt(number))
    for i in range(2, square_root + 1):
        if number % i == 0:
            return False
    return True


def main():
    num = int(input("Enter a positive number to check if it is prime or composite:"))
    if num < 2:
        print(f"{num} is neither prime nor composite. Please enter some number more than or equal to 2")
    elif check_prime_or_not(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is composite")


if __name__ == "__main__":
    main()
