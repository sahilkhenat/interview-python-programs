from utils import input_util


def get_proper_divisors(number: int) -> list[int]:
    proper_divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            proper_divisors.append(i)
            if i != 1 and i != number // i:
                proper_divisors.append(number // i)
    return proper_divisors


def is_perfect_number(number: int) -> bool:
    proper_divisors = get_proper_divisors(number)
    sum_of_divisors = sum(proper_divisors)
    return sum_of_divisors == number


def main():
    number = input_util.get_positive_integer_from_input("Enter a number: ")
    if is_perfect_number(number):
        proper_divisors = get_proper_divisors(number)
        print(
            f"{number} is a perfect number. The sum of proper divisors of {number} ({proper_divisors}) equals {number}.")
    else:
        proper_divisors = get_proper_divisors(number)
        print(
            f"{number} is NOT a perfect number. The sum of proper divisors of {number} ({proper_divisors}) does not equal {number}.")


if __name__ == "__main__":
    main()
