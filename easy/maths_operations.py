"""
Program to perform basic mathematics operations like add, subtract, multiply , divide
"""
def calculate():
    num1 = int(input("Enter 1st number:"))
    num2 = int(input("Enter 2nd number:"))
    choice = int(input("Select operation:\n1.Add \n2.Subtract \n3.Multiply\n4.Divide\n"))
    result = 0

    if choice == 1:
        result= num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice ==3:
        result = num1* num2
    elif choice ==4:
        result = num1/num2
    else:
        print("Select a valid number respective to operation")

    return  result

print("Result is :"+str(calculate()))