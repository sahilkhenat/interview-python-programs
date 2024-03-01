"""
Write a program to Swap Two Numbers: Swap the values of two variables without using a temporary variable.
"""


def swap_two_variables_without_using_temp_variable(a, b):
    a, b = b, a
    return a, b


def main():
    # Using list comprehension to take input for both numbers
    num1, num2 = [int(input(f"Enter number {i + 1}: ")) for i in range(2)]
    print(f"Values before swapping :- num1 = {num1}, num2 ={num2}")
    num1, num2 = swap_two_variables_without_using_temp_variable(num1, num2)
    print(f"Values after swapping :- num1 = {num1}, num2 ={num2}")


if __name__ == "__main__":
    main()
