from Intcode import Machine


with open('inputs/02.in', 'r') as f:
    program = list(map(int, f.readline().split(',')))
nums2 = list(program)
backup = list(program)

program[1] = 12
program[2] = 2

computer = Machine(program)
computer.run()


def part2():
    global nums2
    for noun in range(len(nums2)):
        for verb in range(len(nums2)):
            nums2[1] = noun
            nums2[2] = verb
            computer = Machine(nums2)
            computer.run()
            if computer.data[0] == 19690720:
                return noun*100 + verb

            nums2 = backup


print(f"Position 0: {computer.data[0]}")
print(f"Noun Verb: {part2()}")
