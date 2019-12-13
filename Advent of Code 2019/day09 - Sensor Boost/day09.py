from sys import path
path.append("..")
from Intcode import Machine     # noqa


nums = open('input09.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

print(f"BOOST code: {Machine(nums).run(1)}")
print(f"Coordinates: {Machine(nums).run(2)}")
