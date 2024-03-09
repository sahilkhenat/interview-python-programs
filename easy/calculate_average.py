"""Write a program to Calculate Average: Calculate the average of elements in an array."""


def calculate_average(numbers):
    sum_of_numbers = 0
    for i in numbers:
        sum_of_numbers += i
    average = round((sum_of_numbers/len(numbers)), 2)
    return average


def main():
    input_list = (input("Enter a list of numbers separated by spaces:")).split(sep=' ')
    float_numbers = [float(x) for x in input_list if x.strip()]
    print(f"Average of numbers in given list {float_numbers} = {calculate_average(float_numbers)}")


if __name__ == "__main__":
    main()
