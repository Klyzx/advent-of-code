from itertools import combinations


file = open("inputs/01.in", "r")
numbers = []
for line in file:
    numbers.append(int(line))


def part1(arr):
    combs = combinations(arr, 2)
    for i in combs:
        if sum(i) == 2020:
            return i[0] * i[1]


def part2(arr):
    combs = combinations(arr, 3)
    for i in combs:
        if sum(i) == 2020:
            return i[0] * i[1] * i[2]


print(part1(numbers))
print(part2(numbers))
