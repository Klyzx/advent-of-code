def part1():
    with open("input02.txt") as file:
        twos = 0
        threes = 0
        two = False
        three = False
        for line in file:
            line = line[:-1]
            letters = list(line)
            for char in letters:
                num = letters.count(char)
                if num == 2:
                    two = True
                if num == 3:
                    three = True
            if two:
                twos += 1
                two = False
            if three:
                threes += 1
                three = False
        print("Part 1:", twos*threes)

def part2():
    with open("input02.txt", "r") as file:
        strings = []
        for line in file:
            line = line[:-1]
            strings.append(line)
        for i in range(0,250):
            for j in range(i, 250):
                diff = 0
                str1 = strings[i]
                str2 = strings[j]
                for a, b in zip(str1, str2):
                    if a != b:
                        diff += 1
                if diff == 1:
                    str = ""
                    for a, b in zip(str1, str2):
                        if a == b:
                            str += a
                    print(str)
                    break

part1()
part2()
