"""Write a program to check if given number is even or odd"""


def check_even_or_odd(number):
    if number % 2 == 0:
        return True
    return False


def main():
    num = int(input("Enter a positive number to check if it is prime or composite:"))
    if check_even_or_odd(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


if __name__ == "__main__":
    main()
