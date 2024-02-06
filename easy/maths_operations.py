"""
Program to perform basic mathematics operations like add, subtract, multiply , divide
"""
class Calculator:
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

def main():
    calc = Calculator()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nPerforming basic mathematics operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("\nEnter your choice from following - 1/2/3/4 - ")

    # Switch case
    match choice:
        case "1":
            result = calc.add(num1, num2)
            print(f'Result\n:  {num1} + {num2} = {result}')
        case "2":
            result = calc.subtract(num1, num2)
            print(f'Result\n:  {num1} - {num2} = {result}')
        case "3":
            result = calc.multiply(num1, num2)
            print(f'Result\n:  {num1} * {num2} = {result}')
        case "4":
            result = calc.divide(num1, num2)
            print(f'Result\n:  {num1} / {num2} = {result}')
        case _: print("Please ensure choices are only from 1,2,3, or 4.")


if __name__ == "__main__":
    main()


