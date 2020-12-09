with open("inputs/09.in", "r") as file:
    data = list(map(int, file))

PREAMBLE = 25


def validNumber(goal, numberList):
    for x in numberList:
        if goal - x in numberList:
            return True
    return False


def part1(xmas):
    for i, _ in enumerate(xmas, PREAMBLE):
        if not validNumber(xmas[i], xmas[i - PREAMBLE:i]):
            return xmas[i]


def part2(xmas, invalidNum):
    i = 0
    for begin, _ in enumerate(xmas):
        while sum(xmas[begin:i]) < invalid:
            i += 1
        if sum(xmas[begin:i]) == invalid:
            return min(xmas[begin:i]) + max(xmas[begin:i])


invalid = part1(data)
print(invalid)
print(part2(data, invalid))
