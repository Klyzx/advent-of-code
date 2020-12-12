from Intcode import Machine


with open('inputs/21.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))


computers = [Machine(program, old_input=address) for address in range(50)]
