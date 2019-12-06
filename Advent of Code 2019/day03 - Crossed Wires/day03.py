patha, pathb, _ = open('input03.txt').read().split('\n')
patha, pathb = [x.split(',') for x in [patha, pathb]]

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def wirepath(list):
    x = 0
    y = 0
    length = 0
    ans = {}
    for step in list:
        d = step[0]
        for a in range(int(step[1:])):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


def compare(wirea, wireb):
    return set(wirea) & set(wireb)


pa = wirepath(patha)
pb = wirepath(pathb)
compares = compare(pa, pb)
print(min([abs(x) + abs(y) for (x, y) in compares]))
print(min([pa[p] + pb[p] for p in compares]))
