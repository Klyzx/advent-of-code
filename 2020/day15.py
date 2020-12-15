with open("inputs/15.in") as file:
    numbers = list(map(int, file.readline().strip().split(',')))


def solver(timer):
    spoken_numbers = {}
    last_number = None

    for turn, number in enumerate(numbers):
        spoken_numbers[number] = turn
        last_number = number

    while turn < timer - 1:
        if last_number not in spoken_numbers:
            next_number = 0
        else:
            next_number = turn - spoken_numbers[last_number]

        spoken_numbers[last_number] = turn
        last_number = next_number
        turn += 1
    return last_number


print(solver(2020))
print(solver(30000000))
