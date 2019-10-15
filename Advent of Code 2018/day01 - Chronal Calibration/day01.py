file = open("input01.txt", "r")


def part1():
    sum = 0
    for line in file:
        line = int(line)
        sum += line
    print("Part 1:", sum) 

file.seek(0,0)

def part2():
    numbers = []
    sum = 0
    loop = True
    while loop:
        for line in file:
            line = int(line)
            sum += line
            if sum not in numbers:
                numbers.append(sum)
            else:
                print("Part 2:", sum)
                file.close()
                loop = False
                break
        else:
            file.seek(0, 0)


part1()
part2()
