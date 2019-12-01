import math
file = open("input01.txt", "r")

def day01():
    a = 0
    b = 0
    for line in file:
        x = math.floor(int(line)/3) - 2
        a += x
        while (x > 0):
            b += x
            x = math.floor(int(x)/3) - 2
    return(a, b)

print(day01())
file.close()
