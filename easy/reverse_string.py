"""String Reversal: Write a function to reverse a string without using built-in functions."""


def reverse_string(s):
    return s[::-1]


def main():
    input_string = input("Enter the string that you want to reverse:")
    reversed_string = reverse_string(input_string)
    print(f'Reverse of {input_string} is : {reversed_string}')

if __name__ == "__main__":
    main()