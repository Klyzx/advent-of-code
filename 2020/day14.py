from collections import defaultdict


with open("inputs/14.in", "r") as file:
    directions = file.read().splitlines()


def part1(array):
    mem = defaultdict(int)
    for _, line in enumerate(array):
        line = line.split(' = ')
        # Change mask
        if line[0] == "mask":
            mask = int(line[1].replace('0', '1').replace('X', '0'), 2)
            newvalue = int(line[1].replace('X', '0'), 2)
        # Change value
        else:
            value = int(line[1])
            index = int(line[0][4:-1])
            value = (value & ~mask) | (newvalue & mask)

            # Set to memory
            mem[index] = value
    return mem


def addresses(x):
    if 'X' not in x:
        yield x
    else:
        yield from addresses(x.replace('X', '0', 1))
        yield from addresses(x.replace('X', '1', 1))


def part2(array):
    mem = defaultdict(int)
    for _, line in enumerate(array):
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1]
        else:
            a = "{0:036b}".format(int(line[0][4:-1]))
            x = ''.join([x if x != "0" else a[i] for i, x in enumerate(mask)])
            for k in addresses(x):
                mem[int(k, 2)] = int(line[1])
    return mem


memory1 = part1(directions)
print(sum([memory1[key] for key in memory1]))
memory2 = part2(directions)
print(sum([memory2[key] for key in memory2]))
