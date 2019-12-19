from Intcode import Machine


with open('inputs/19.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))


def findsquare():
    for y in range(900, 1300):
        for x in range(900, 1300):
            drone = Machine(program)
            drone.set_input([x, y])
            results = drone.run()
            if results == 0:
                continue
            if Machine(program, [x + 99, y - 99]).run() == 1:
                return x*10000 + y - 99
            break


findsquare()
