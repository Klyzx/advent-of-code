from copy import deepcopy
import numpy as np


def printgrid():
    for y in range(1, 6):
        for x in range(1, 6):
            z = grid[y][x]
            if z == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()
    print()


def biodiversity():
    bio = 0
    cell = 0
    for y in range(1, 6):
        for x in range(1, 6):
            bio += grid[y][x]*(2**cell)
            cell += 1
    return bio


grid = np.array([[1, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [1, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [1, 1, 0, 1, 0]])

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

grid = np.pad(grid, (1), 'constant', constant_values=(0)).tolist()

repeats = []
while grid not in repeats:
    repeats.append(grid)
    newgrid = deepcopy(grid)
    for y in range(1, 6):
        for x in range(1, 6):
            bugs = 0
            for offset in directions:
                bugs += grid[y + offset[0]][x + offset[1]]
            if grid[y][x] == 0 and (bugs == 1 or bugs == 2):
                newgrid[y][x] = 1
            elif grid[y][x] == 1 and bugs != 1:
                newgrid[y][x] = 0
    # printgrid()
    grid = deepcopy(newgrid)


printgrid()
print(biodiversity())
