"""
Compute the nth fibonacci number with a bottom-up approach to dynamic programming.

Fill in a list of values by adding the previous two entries each iteration of a for loop.

Similar to the memoization approach, a calculation is performed for every element in the fib sequence, therefore running in O(n).
"""


def fib(n):
    # Initialize fib sequence with base cases
    return fib_tab(n - 1, sequence=[0, 1])


def fib_tab(n, sequence):
    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence[n]


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

    result = fib(n)
    print(f"The ({n}) fibonacci number is {result}.")
