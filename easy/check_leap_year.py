"""Write a program to check if given year is a leap year or not."""


def is_leap_year(year):
    if (year % 4 == 0 and year %100 !=0) or (year % 400 == 0):
        return True
    else:
        return False


def main():
    year = int(input("Enter year that you want to check if it is leap or not:"))
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


if __name__ == "__main__":
    main()
