from sys import path
path.append("..")
from Intcode import Machine     # noqa


nums = open('input09.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])

print(f"BOOST keycode: {Machine(nums, None).run(1)}")
print(f"Coordinates: {Machine(nums, None).run(2)}")
