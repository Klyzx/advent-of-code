INPUT = '963275481'


def make_ring(input, part2=False):
    input = [int(x) for x in str(INPUT)]
    if part2:
        for x in range(10, 1000001):
            input.append(x)
    current = input[0]
    ring = {}
    for i in range(len(input)):
        if i == len(input) - 1:
            ring[input[i]] = input[0]
        else:
            ring[input[i]] = input[i+1]
    return ring, current


def round(ring, current, maximum=9):
    next_num = ring[current]
    pick_up = [None, None, None]
    for i in range(3):
        pick_up[i] = next_num
        next_num = ring[next_num]
    ring[current] = next_num

    destination_cup = current
    while destination_cup in pick_up or destination_cup == current:
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = maximum

    ring[pick_up[2]] = ring[destination_cup]
    ring[destination_cup] = pick_up[0]

    return ring, next_num


ring, current = make_ring(INPUT, part2=True)

for _ in range(10000000):
    ring, current = round(ring, current, maximum=1000000)

print(ring[1] * ring[ring[1]])
