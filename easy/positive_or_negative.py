"""Write a program to check if given number is positive or negative."""


def check_positive_or_negative(number):
    if number > 0:
        return True
    return False


def main():
    num = int(input("Enter a number for which you want to check if it is positive or negative: "))
    if num == 0:
        print("Given number is 0. It is neither positive nor negative")
    else:
        if check_positive_or_negative(num):
            print(f"{num} is positive")
        else:
            print(f"{num} is negative")


if __name__ == "__main__":
    main()