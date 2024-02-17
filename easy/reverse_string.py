"""String Reversal: Write a function to reverse a string with all possible ways that you can think of."""


# Using slicing
def reverse_string_by_slicing(s):
    return s[::-1]


# Using built-in reversed() function
def reverse_using_builtin_functions(s):
    return ''.join(reversed(s))


# Using for loop
def reverse_using_for_loop(s):
    reversed_string = ""
    for i in s:
        reversed_string = i + reversed_string
    return reversed_string


def main():
    input_string = input("Enter the string that you want to reverse:")
    reversed_string_slicing = reverse_string_by_slicing(input_string)
    reversed_string_built_in = reverse_using_builtin_functions(input_string)
    reversed_string_for_loop = reverse_using_for_loop(input_string)
    print(f'Reverse of {input_string} using slicing is : {reversed_string_slicing}')
    print(f'Reverse of {input_string} using built in function is : {reversed_string_built_in}')
    print(f'Reverse of {input_string} using for loop is : {reversed_string_for_loop}')


if __name__ == "__main__":
    main()
