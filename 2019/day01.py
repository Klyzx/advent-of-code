file = open("inputs/01.in", "r")


def day01():
    a = 0
    b = 0
    for line in file:
        x = int(line)//3 - 2
        a += x
        while (x > 0):
            b += x
            x = x//3 - 2
    return(a, b)


print(day01())
file.close()
