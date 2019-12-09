from sys import path
path.append("..")
from Intcode import Machine # noqa


nums = open('input02.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums2 = list(nums)
backup = list(nums)

nums[1] = 12
nums[2] = 2

computer = Machine(nums)
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
