"""
Program to display the fibonacci series n-th term
"""
def fibonacci(n):
    # first two terms
    n1, n2 = 0,1
    print("Fibonacci series:",n1,n2,end=",")
    for i in range (2,n):
        n3 = n1+n2
        n1 =n2
        n2 =n3
        if n3 !=None:
            print(n3,end=",")

print(fibonacci(9))