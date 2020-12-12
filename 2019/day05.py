from Intcode import Machine


with open('inputs/05.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))

machine1 = Machine(program, [1])
machine2 = Machine(program, [5])

while machine1.running:
    out1 = machine1.run()
while machine2.running:
    out2 = machine2.run()

print(f"Diagnostic Code 1: {out1}")
print(f"Diagnostic Code 5: {out2}")
