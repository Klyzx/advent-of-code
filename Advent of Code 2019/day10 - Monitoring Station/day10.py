from math import gcd, atan2, degrees
import itertools


with open('input10.txt') as file:
    input = file.read().strip()
    asteroids = [(x, y) for y, line in enumerate(input.split())
                 for x, c in enumerate(line) if c == "#"]


def visible(source, asteroids):
    targets = {}
    for target in asteroids:
        if target == source:
            continue
        dx = target[0] - source[0]
        dy = target[1] - source[1]
        dist = gcd(abs(dx), abs(dy))
        dx /= dist
        dy /= dist
        targets[(dx, dy)] = ((dist, target))
    return targets


def besttargets(asteroids):
    besttargets = {}
    bestasteroid = (0, 0)
    for i in range(len(asteroids)):
        targets = visible(asteroids[i], asteroids)
        if len(targets) > len(besttargets):
            besttargets = targets
            bestasteroid = asteroids[i]

    return besttargets, bestasteroid


def angler(direction):
    return (degrees(atan2(direction[1], direction[0])) + 90) % 360


a, b = besttargets(asteroids)
print(len(a))


directions = list(a)
directions.sort(key=angler)
target = next(itertools.islice(directions, 199, None))
print(target[0] * 100 + target[1] + b[0]*100 + b[1])
