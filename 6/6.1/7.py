import numpy as np


def make_board(n):
    board = np.zeros((n, n), dtype=np.int8)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i][j] = 1
    return board


n = int(input())
print(make_board(n))
