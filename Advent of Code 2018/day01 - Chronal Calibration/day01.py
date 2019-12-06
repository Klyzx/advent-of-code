file = open("input01.txt", "r")


def part1():
    sum = 0
    for line in file:
        line = int(line)
        sum += line
    return (sum)


def part2():
    numbers = []
    sum = 0
    while True:
        for line in file:
            line = int(line)
            sum += line
            if sum not in numbers:
                numbers.append(sum)
            else:
                return (sum)
        else:
            file.seek(0, 0)


print(part1())
file.seek(0, 0)
print(part2())

file.close()
