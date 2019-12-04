import sys
sys.path.append("..")
from Intcode import opcod

file = open("input02.txt", "r")

def input():
    line = file.readline()
    line = line.split(',')
    arr = [int(i.strip()) for i in line]
    file.seek(0,0)
    return arr

def part2(arr, goal):
    for noun in range(0, len(arr)):
        for verb in range(0, len(arr)):
            arr[1] = noun
            arr[2] = verb
            x = opcod(arr, 1)
            if x == goal:
                return (noun, verb)
            arr = input()

inp1 = input()
inp1[1] = 12
inp1[2] = 2
print(opcod(inp1, 1))

inp2 = input()
x, y = part2(inp2, 19690720)
print(100*x + y)
