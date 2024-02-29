"""Sum of Digits: Write a function to calculate the sum of digits of a given positive number."""


def sum_of_digits(n):
    num = n
    sum_of_all_digits = 0
    while num > 0:
        remainder = num % 10
        sum_of_all_digits = sum_of_all_digits + remainder
        num = num // 10
    return sum_of_all_digits


def main():
    try:
        number_input = input("Enter a positive number to find sum of its digits- ")
        if not number_input.isdigit():
            raise TypeError("Given value is either negative number or string. Please enter a positive number.")
        else:
            number = int(number_input)
            if number >=0:
                sum_digits = sum_of_digits(number)
                print(f"Sum of digits in {number} = {sum_digits}")
    except TypeError as te:
        print(te)


if __name__ == "__main__":
    main()
