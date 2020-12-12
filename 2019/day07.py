from Intcode import Machine
from itertools import permutations


with open('inputs/07.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))


def part1():
    max_output = 0
    for phases in permutations([0, 1, 2, 3, 4]):
        amplifiers = [Machine(program, old_input=phase) for phase in phases]
        out_in = 0
        for amplify in amplifiers:
            out_in = amplify.run(old_input=out_in)
        max_output = max(max_output, out_in)
    return max_output


def part2():
    max_output = 0
    for phases in permutations([5, 6, 7, 8, 9]):
        amplifiers = [Machine(program, old_input=phase) for phase in phases]
        out_in = 0
        while amplifiers[0].running:
            for amplify in amplifiers:
                out_in = amplify.run(old_input=out_in)
                max_output = max(max_output, out_in)
    return max_output


print(f"Max thrust: {part1()}")
print(f"Feedback loop thrust: {part2()}")
