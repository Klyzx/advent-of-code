from sys import path
path.append("..")
from Intcode import Machine # noqa


nums = open('input05.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

machine1 = Machine(nums, 1)
machine2 = Machine(nums, 5)
out1 = 0
out2 = 0

while machine1.running:
    out1 = machine1.run()
while out2 == 0:
    out2 = machine2.run()

print(f"Diagnostic Code 1: {out1}")
print(f"Diagnostic Code 5: {out2}")
