from copy import deepcopy
from math import gcd


mp = []
mv = []
for line in open("inputs/12.in", "r").readlines():
    line = (line.strip())[1:-1].strip().split()
    moon = {}
    for val in line:
        k, v = val.split('=')
        if v.endswith(','):
            v = v[:-1]
        moon[k] = int(v)
    mp.append(moon)
    mv.append({'x': 0, 'y': 0, 'z': 0})

mp2 = deepcopy(mp)
mv2 = deepcopy(mv)


def move(pos, vel):
    for i in range(len(pos)):
        for j in range(len(vel)):
            for k in pos[i]:
                if pos[i][k] > pos[j][k]:
                    vel[i][k] -= 1
                elif pos[i][k] < pos[j][k]:
                    vel[i][k] += 1
    for i in range(len(pos)):
        for k in pos[i]:
            pos[i][k] += vel[i][k]


for _ in range(1000):
    move(mp, mv)

energy = 0
for i in range(len(mp)):
    pot = 0
    kin = 0
    for k in mp[i]:
        pot += abs(mp[i][k])
        kin += abs(mv[i][k])
    energy += pot*kin
print(energy)


def lcm(x, y):
    return x * y // gcd(x, y)


seen = {k: {} for k in mp2[0]}
found = {k: False for k in mp2[0]}
cycle = 0
p2 = 1
cyclesfound = 0
while cyclesfound < 3:
    move(mp2, mv2)
    positions = {k: [] for k in mp2[0]}
    for i in range(len(mp2)):
        for k in mp2[i]:
            positions[k].append(mp2[i][k])
            positions[k].append(mv2[i][k])
    positions = {k: tuple(v) for k, v in positions.items()}
    for k in positions:
        if positions[k] in seen[k]:
            if not found[k]:
                p2 = lcm(p2, cycle)
                cyclesfound += 1
                found[k] = True
        seen[k][positions[k]] = cycle
    cycle += 1


print(p2)
