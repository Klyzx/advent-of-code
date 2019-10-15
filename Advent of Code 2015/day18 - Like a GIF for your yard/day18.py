import numpy as np
size = 102
steps = 99

board = np.zeros((size, size), dtype=np.int)
seed = []

with open("input18.txt") as f:
    for line in f:
        line = list(line)
        del line[-1]
        line = [int(x) for x in line]
        seed.append(line)

board[1:size - 1, 1:size - 1] = seed


def survive():
    global board
    newboard = np.zeros((size, size), dtype=np.int)
    for i in range(0, size):
        for j in range(0, size):
            neighbors = np.sum(board[i - 1:i + 2, j - 1:j + 2]) - board[i, j]
            if board[i, j] == 0 and neighbors == 3:
                newboard[i, j] = 1
            elif board[i, j] == 1 and (neighbors == 2 or neighbors == 3):
                newboard[i, j] = 1
            else:
                newboard[i, j] = 0
    board = np.zeros((size, size), dtype=np.int)
    board[1:size - 1] = newboard[1:size - 1]


for k in range(100):
    survive()

print(np.sum(board))
