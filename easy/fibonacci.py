"""
Program to display the fibonacci series n-th term using iteration
"""


from utils import input_util


def fibonacci_series(number):
    # Initialize the first two terms
    n1, n2 = 0, 1
    fib_series = [n1, n2]

    # Generate Fibonacci series
    for _ in range(2, number):
        n3 = n1 + n2
        fib_series.append(n3)
        n1, n2 = n2, n3

    return fib_series


def main():
    # Get the number of terms in Fibonacci series from user input
    num_terms = input_util.get_positive_integer_from_input("number of terms in Fibonacci series: ")

    # Calculate Fibonacci series
    fib_series = fibonacci_series(num_terms)

    # Print the Fibonacci series
    print(f"Fibonacci series with {num_terms} terms: {fib_series}")


if __name__ == "__main__":
    main()

