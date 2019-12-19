with open('inputs/16.in', 'r') as f:
    number = list(map(int, f.readline().strip()))


pattern = [0, 1, 0, -1]


def multiplier(index, iteration):
    return pattern[((index + 1) // (iteration+1)) % 4]


def part1func(num):
    output = []
    for i in range(len(num)):
        dsum = 0
        for j in range(len(num)):
            dsum += num[j] * multiplier(j, i)
        output.append(abs(dsum) % 10)

    return output


def part2func(num):
    s = sum(num)
    output = []
    for i in range(len(num)):
        output.append(s % 10)
        s -= num[i]

    return output


part1 = list(number)
for _ in range(100):
    part1 = part1func(part1)


print(''.join(map(str, part1[:8])))


part2 = list(number)
offset = int("".join(map(str, number[:7])))
part2 *= 10000
part2 = part2[offset:]

for _ in range(100):
    part2 = part2func(part2)

print(''.join(map(str, part2[:8])))
