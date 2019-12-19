from collections import defaultdict
from math import ceil
import re
pattern = r'((?:\d+ [A-Z]+, )*\d+ [A-Z]+) => (\d+) ([A-Z]+)'


def get_reactions():
    with open("inputs/14.in", "r") as f:
        reactions = {}
        input = f.read().rstrip()
        for line in input.split('\n'):
            match = re.search(pattern, line)
            output_amount = int(match.group(2))
            output = match.group(3)
            inputs = []
            for input in match.group(1).split(', '):
                input_amount, input = input.split(' ')
                inputs.append((int(input_amount), input))
            reactions[output] = (output_amount, inputs)
    return reactions


def ore_req(reactions, reactant, reactant_amount, surplus=None):
    if surplus is None:
        surplus = defaultdict(int)
    if reactant == "ORE":
        return reactant_amount
    elif reactant_amount <= surplus[reactant]:
        surplus[reactant] -= reactant_amount
        return 0
    reactant_amount -= surplus[reactant]
    surplus[reactant] = 0
    ore = 0
    output_amount = reactions[reactant][0]
    make_up_reactions = reactions[reactant][1]
    repeat = ceil(reactant_amount / output_amount)
    for new_amount, new_reactant in make_up_reactions:
        new_amount *= repeat
        ore += ore_req(reactions, new_reactant, new_amount, surplus)
    surplus[reactant] = output_amount * repeat - reactant_amount
    return ore


react = get_reactions()


def part1():
    return ore_req(react, "FUEL", 1)


def part2():
    high = 10**7
    low = 1
    mid = (high + low) // 2
    while low < high:
        if ore_req(react, "FUEL", mid) > 1000000000000:
            high = mid - 1
        else:
            low = mid
        mid = (high + low) // 2
    return low


print(part1())
print(part2())
