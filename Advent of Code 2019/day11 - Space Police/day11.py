from collections import defaultdict
from sys import path
import numpy as np
path.append("..")
from Intcode import Machine     # noqa

DX = {0: 0, 1: 1, 2: 0, 3: -1}
DY = {0: 1, 1: 0, 2: -1, 3: 0}

program = open('input11.txt').read().split(',')
for i in range(len(program)):
    program[i] = int(program[i])

robot = Machine(program)
robot2 = Machine(program)


def paintbot(robo, start):
    paint = defaultdict(int)
    positionl = [0, 0]
    positiont = (0, 0)
    curpaint = 0
    direction = 0
    paint[positiont] = start
    while robo.running:
        curpaint = robo.run(paint[positiont])
        direction += (2*robo.run())-1
        paint[positiont] = curpaint
        positionl[0] += DX[direction % 4]
        positionl[1] += DY[direction % 4]
        positiont = tuple(positionl)
    return paint


print(f"Part 1: {len(paintbot(robot, 0))}")


paint2 = paintbot(robot2, 1)

arr = np.zeros((6, 43), dtype=int)
for y in range(6):
    for x in range(43):
        listy = [x, y-5]
        arr[5-y][x] = paint2[tuple(listy)]


for item in arr:
    print(item)

print("Some assembly required")
