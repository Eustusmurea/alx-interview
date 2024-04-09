#!/usr/bin/python3
""" N queens puzzle, challenge of placing N non attacking queens
on a NxN chessboard
This program solves the N queens problem """

import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N):
    def solve(board, row):
        if row >= N:
            return [board[:]]

        solutions = []
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solutions += solve(board, row + 1)
                board[row] = -1

        return solutions

    # Initialize board with all positions as -1
    board = [-1] * N
    solutions = solve(board, 0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
