from sys import path
path.append("..")
from Intcode import Machine     # noqa


with open('input13.txt', 'r') as f:
    program = list(map(int, f.readline().split(',')))

x = []
y = []
tile = []
Breakout = Machine(program)

while Breakout.running:
    x.append(Breakout.run())
    y.append(Breakout.run())
    tile.append(Breakout.run())

print(tile.count(2))

Breakout2 = Machine(program)
Breakout2.data[0] = 2
score = 0
px = x[tile.index(3)]
bx = x[tile.index(4)]
while Breakout2.running:
    move = 1 if px < bx else -1 if px > bx else 0
    x = Breakout2.run(move)
    y = Breakout2.run()
    z = Breakout2.run()
    if x == -1 and y == 0:
        score = z
    if z == 3:
        px = x
    elif z == 4:
        bx = x
print(score)
