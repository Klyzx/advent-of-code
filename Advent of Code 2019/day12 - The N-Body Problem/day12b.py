from copy import deepcopy
import math

MP = []
MV = []
for line in open('input12.txt').readlines():
    line = line.strip()
    line = line[1:-1]
    words = line.split()
    moon = {}
    for w in words:
        k, v = w.split('=')
        if v.endswith(','):
            v = v[:-1]
        moon[k] = int(v)
    MP.append(moon)
    MV.append({'x': 0, 'y': 0, 'z': 0})


def tick():
    for i in range(len(MP)):
        for j in range(len(MP)):
            for k in MP[i]:
                if MP[i][k] < MP[j][k]:
                    MV[i][k] += 1
                if MP[i][k] > MP[j][k]:
                    MV[i][k] -= 1
    for i in range(len(MP)):
        for k in MP[i]:
            MP[i][k] += MV[i][k]


OLD_MP = deepcopy(MP)
OLD_MV = deepcopy(MV)
for _ in range(1000):
    tick()
p1 = 0
for i in range(len(MP)):
    pot = 0
    kin = 0
    for k in MP[i]:
        pot += abs(MP[i][k])
        kin += abs(MV[i][k])
    p1 += pot*kin
print(p1)

MP = OLD_MP
MV = OLD_MV
SEEN = {k: {} for k in MP[0]}
CNT = {k: 0 for k in MP[0]}
t = 0
p2 = 1
p2_cnt = 0
while p2_cnt < 3:
    tick()
    KEY = {k: [] for k in MP[0]}
    for i in range(len(MP)):
        for k in MP[i]:
            KEY[k].append(MP[i][k])
            KEY[k].append(MV[i][k])
    KEY = {k: tuple(v) for k, v in KEY.items()}
    for k in KEY:
        if KEY[k] in SEEN[k]:
            if CNT[k] == 0:
                p2 = p2*t//math.gcd(p2, t)
                p2_cnt += 1
                if p2_cnt == 3:
                    print(p2)
                    break
            CNT[k] += 1
        SEEN[k][KEY[k]] = t
    t += 1
