#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve_nqueens(board, row + 1, N, solutions)

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)
