from collections import defaultdict
import re


with open("inputs/07.in", "r") as file:
    bagData = file.read().splitlines()

contains = defaultdict(list)
containedIn = defaultdict(set)
for bagInfo in bagData:
    color = re.match(r'(.+) bags contain', bagInfo)[1]
    for count, containColors in re.findall(r'(\d+) (.+?) bags?[,.]', bagInfo):
        count = int(count)
        containedIn[containColors].add(color)
        contains[color].append((count, containColors))


shinygold = set()


def check(color):
    for c in containedIn[color]:
        shinygold.add(c)
        check(c)


def totalBags(color):
    total = 0
    for count, containColor in contains[color]:
        total += count
        total += count * totalBags(containColor)
    return total


check('shiny gold')
print(len(shinygold))
print(totalBags('shiny gold'))
