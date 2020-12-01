from math import prod


file = open("inputs/01.in", "r")
data = list(map(int, file))


def part1(arr):
    return [x for x in data if 2020 - x in data]


def part2(arr):
    return set([x for x in data for y in data if 2020 - x - y in data])


print(prod(part1(data)))
print(prod(part2(data)))
