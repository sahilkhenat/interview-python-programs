"""
Program to display the fibonacci series n-th term using iteration
"""


def fibonacci(n=10):
    # first two terms
    n1, n2 = 0, 1
    fib_series = [n1, n2]

    for _ in range(2, n):
        n3 = n1 + n2
        fib_series.append(n3)
        n1, n2 = n2, n3
    return fib_series


print(fibonacci(10))
