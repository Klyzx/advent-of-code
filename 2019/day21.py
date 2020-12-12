from Intcode import Machine


with open('inputs/21.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))


walks = [ord(c) for c in '\n'.join([
    "NOT A J",
    "NOT B T",
    "OR T J",
    "NOT C T",
    "OR T J",
    "AND D J",
    "WALK\n"
  ])]
springwalk = Machine(program, walks)
while springwalk.running:
    x = springwalk.run()
    if x < 256:
        print(chr(x), end='')
print(f"Part 1: {x}")

runs = [ord(c) for c in '\n'.join([
    "NOT A J",
    "NOT B T",
    "OR T J",
    "NOT C T",
    "OR T J",
    "AND D J",  # Part 1
    "NOT E T",
    "NOT T T",
    "OR H T",
    "AND T J",
    "RUN\n"
    ])]
springrun = Machine(program, runs)
while springrun.running:
    y = springrun.run()
    if y < 256:
        print(chr(y), end='')


print(f"Part 2: {y}")
