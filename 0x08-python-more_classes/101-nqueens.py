#!/usr/bin/python3
import sys

def print_usage_and_exit():

    # Print the correct usage and exit with status 1
    print("Usage: nqueens N")
    sys.exit(1)

def solve_nqueens(N, queens, row):
    # Base case: If all queens are placed, print the solution
    if row == N:
        print(queens)
        return

    # Recursive case: Try placing a queen in each column of the current row
    for col in range(N):
        # Check if placing a queen at the current position is valid
        valid = all(
            col != queen[1] and
            abs(row - queen[0]) != abs(col - queen[1])
            for queen in queens
        )

        # If valid, place the queen and move on to the next row
        if valid:
            queens.append([row, col])
            solve_nqueens(N, queens, row + 1)
            queens.pop()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        # Parse N from the command line argument
        N = int(sys.argv[1])
    except ValueError:
        # If N is not an integer, print an error message and exit
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty list to store the queen positions
    queens = []

    # Start solving the N queens problem
    solve_nqueens(N, queens, 0)
