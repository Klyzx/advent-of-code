with open("inputs/12.in", "r") as file:
    directions = file.read().splitlines()


def part1():
    shipPosition = 0 + 0j
    direction = 1 + 0j
    for line in directions:
        move, distance = line[:1], int(line[1:])
        if move == "N":
            shipPosition += distance * 1j
        elif move == "S":
            shipPosition -= distance * 1j
        elif move == "E":
            shipPosition += distance
        elif move == "W":
            shipPosition -= distance
        elif move == "L":
            direction *= 1j**(distance/90)
        elif move == "R":
            direction /= 1j**(distance/90)
        elif move == "F":
            shipPosition += direction * distance
    return (shipPosition.real, shipPosition.imag)


def part2():
    shipPosition = 0 + 0j
    waypoint = 10 + 1j
    for line in directions:
        move, distance = line[:1], int(line[1:])
        if move == "N":
            waypoint += distance * 1j
        elif move == "S":
            waypoint -= distance * 1j
        elif move == "E":
            waypoint += distance
        elif move == "W":
            waypoint -= distance
        elif move == "L":
            waypoint *= 1j**(distance/90)
        elif move == "R":
            waypoint /= 1j**(distance/90)
        elif move == "F":
            shipPosition += distance * waypoint
    return (shipPosition.real, shipPosition.imag)


a = part1()
b = part2()
print(a, (abs(a[0]) + abs(a[1])))
print(b, (abs(b[0]) + abs(b[1])))
