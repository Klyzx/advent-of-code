from Intcode import Machine


with open('inputs/09.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))

print(f"BOOST code: {Machine(program, [1]).run()}")
print(f"Coordinates: {Machine(program, [2]).run()}")
