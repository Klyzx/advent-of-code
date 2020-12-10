from collections import defaultdict


with open("inputs/10.in", "r") as file:
    data = list(map(int, file))
data.append(0)
data.append(max(data)+3)
data.sort()


def part1(voltages):
    diff_list = []
    for x, y in zip(voltages[0:], voltages[1:]):
        diff_list.append(y-x)
    return diff_list.count(1)*diff_list.count(3)


adapterDict = defaultdict(int)
adapterDict[0] = 1
for i in data[1:]:
    adapterDict[i] = adapterDict[i-1] + adapterDict[i-2] + adapterDict[i-3]


print(f'Part 1: {part1(data)}')
print(f'Part 2: {adapterDict[max(data)]}')
