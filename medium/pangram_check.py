"""
Check if a String is a Pangram
A pangram is a string that contains every letter of the alphabet at least once.
Example : "The quick brown fox jumps over the lazy dog";
"""
import string

from utils import input_util


def pangram_check(input_string):
    """Checks if a string is a pangram (contains every letter of the alphabet at least once)."""

    alphabets = set(string.ascii_letters.lower())  # Case-insensitive alphabet set
    lower_case_string_without_spaces = "".join(input_string.lower().split())

    # Check if all alphabets are present in the string (at least once)
    is_pangram = all(char in lower_case_string_without_spaces for char in alphabets)
    return is_pangram


def main():
    input_string = input_util.get_string_from_input("string")
    if pangram_check(input_string):
        print(f"{input_string} is a pangram")
    else:
        print(f"'{input_string}' is not a pangram")


if __name__ == "__main__":
    main()
