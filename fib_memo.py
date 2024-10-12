"""
Use dynamic programming to print the nth number of the fibonacci sequence. 

Top-down approach results in a recursive tree, whose left leaf is fib(n-1) and right fib(n-2) until reaching base cases n == 0 and n == 1, returning 0 and 1 respectively.

Utilize a memoization table to reduce runtime. Checks memoization table before calculating, simply retrieving value. Store results of new calculations. 

Without memoization, fib(n) has to repeat calculations at every subproblem and since every subproblem branches into two more subproblems a number n times, this runs in O(2^n).

With memoization, calculations are not repeated. n calculations are performed, and memoization table retrievals are constant. O(n).

"""


def fib(n):
    # Wrapper function to initialize with memoization with base cases.
    return fib_memo(n, [0, 1])


def fib_memo(n, memo):
    if n in memo:
        # Retrieve memoized value
        return memo[n]
    else:
        # Calculate value
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # Ask for a number n, print corresponding fib number
    while True:
        # keep asking until an integer given
        try:
            n = int(input("Which value of the fibonacci sequence are you looking for?"))
            if n > 0:
                break
            else:
                print("Must be a positive, whole number.")

        except ValueError:
            print("Must be a positive, whole number.")

    result = fib(n - 1)
    print(f"The ({n}) fibonacci number is {result}.")
