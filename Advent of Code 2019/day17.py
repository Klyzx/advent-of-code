from Intcode import Machine


with open('inputs/17.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))

# L10 L12 R6 - A
# R10 L4 L4 L12 - B
# L10 R10 R6 L4 - C
# A B A B A C B C A C

# 76 44 53 44 53 44 76 44 54 44 54 44 82 44 54
# 82 44 53 44 53 44 76 44 52 44 76 44 52 44 76 44 54 44 54
# 76 44 53 44 53 44 82 44 53 44 53 44 82 44 54 44 76 44 52
# 65 44 66 44 65 44 66 44 65 44 67 44 66 44 67 44 65 44 67


inputs = [ord(c) for c in '\n'.join([
  "A,B,A,B,A,C,B,C,A,C",
  "L,10,L,12,R,6",
  "R,10,L,4,L,4,L,12",
  "L,10,R,10,R,6,L,4",
  "n\n"])]
robot = Machine(program, inputs)
robot.data[0] = 2
while robot.running:
    x = robot.run()
    if x < 256:
        print(chr(x), end='')

print(x)
