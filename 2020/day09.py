with open("inputs/09.in", "r") as file:
    data = list(map(int, file))

PREAMBLE = 25


def valid_number(goal, number_list):
    for num in number_list:
        if goal - num in number_list:
            return True
    return False


def part1(xmas):
    for i, _ in enumerate(xmas, PREAMBLE):
        if not valid_number(xmas[i], xmas[i - PREAMBLE:i]):
            return xmas[i]


def part2(xmas, invalid_num):
    i = 0
    for begin, _ in enumerate(xmas):
        while sum(xmas[begin:i]) < invalid_num:
            i += 1
        if sum(xmas[begin:i]) == invalid_num:
            return min(xmas[begin:i]) + max(xmas[begin:i])


invalid = part1(data)
print(invalid)
print(part2(data, invalid))
