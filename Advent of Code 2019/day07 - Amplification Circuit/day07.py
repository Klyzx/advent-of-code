from itertools import permutations
from sys import path
path.append("..")
from Intcode import Machine # noqa


nums = open('input07.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])


def part1():
    max_output = 0
    for phases in permutations([0, 1, 2, 3, 4]):
        amplifiers = [Machine(nums, phase) for phase in phases]
        out_in = 0
        for amplify in amplifiers:
            out_in = amplify.run(out_in)
        max_output = max(max_output, out_in)
    return max_output


def part2():
    max_output = 0
    for phases in permutations([5, 6, 7, 8, 9]):
        amplifiers = [Machine(nums, phase) for phase in phases]
        out_in = 0
        while amplifiers[0].running:
            for amplify in amplifiers:
                out_in = amplify.run(out_in)
                max_output = max(max_output, out_in)
    return max_output


print(f"Max thrust: {part1()}")
print(f"Feedback loop thrust: {part2()}")
