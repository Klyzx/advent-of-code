with open("inputs/12.in", "r") as file:
    directions = file.read().splitlines()


def part1():
    ship_position = 0 + 0j
    direction = 1 + 0j
    for line in directions:
        move, distance = line[:1], int(line[1:])
        if move == "N":
            ship_position += distance * 1j
        elif move == "S":
            ship_position -= distance * 1j
        elif move == "E":
            ship_position += distance
        elif move == "W":
            ship_position -= distance
        elif move == "L":
            direction *= 1j**(distance/90)
        elif move == "R":
            direction /= 1j**(distance/90)
        elif move == "F":
            ship_position += direction * distance
    return (ship_position.real, ship_position.imag)


def part2():
    ship_position = 0 + 0j
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
            ship_position += distance * waypoint
    return (ship_position.real, ship_position.imag)


a = part1()
b = part2()
print(a, (abs(a[0]) + abs(a[1])))
print(b, (abs(b[0]) + abs(b[1])))
