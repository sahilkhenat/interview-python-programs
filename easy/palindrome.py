"""Palindrome Check: Write a function to check if a given string is a palindrome."""


def palindrome_check(s):
    if s == s[::-1]:
        return True
    else:
        return False


def main():
    input_string = input("Enter string for which you have to perform palindrome check :")
    if palindrome_check(input_string):
        print(f'{input_string} is a PALINDROME')
    else:
        print(f'{input_string} is NOT a PALINDROME')


if __name__ == "__main__":
    main()
