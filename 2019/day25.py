from Intcode import Machine


with open('inputs/25.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))


textbot = Machine(program, day=25)

while textbot.running:
    x = textbot.run()
    if x < 256:
        print(chr(x), end='')
