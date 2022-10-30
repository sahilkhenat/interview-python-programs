"""
Program to display the fibonacci series n-th term using iteration
"""
def fibonacci():
    # first two terms
    n = 10
    n1, n2 = 0,1
    print("Fibonacci series:",n1,n2,end=",")
    for i in range (2,n):
        n3 = n1+n2
        n1 =n2
        n2 =n3
        if n3 !=None:
            print(n3,end=",")

print(fibonacci())