from sys import exit
from itertools import permutations
ADV = {1: 4, 2: 4, 3: 2, 4: 0, 5: 0, 6: 0, 7: 4, 8: 4}


class Machine:
    def __init__(self, data, phase):
        self.data = list(data)
        self.IP = 0
        self.write(1, phase)
        self.IP += 2

    def run(self, input=None):
        while self.running:
            cmd = self.data[self.IP] % 100

            if cmd == 1:
                self.write(3, self.get(1) + self.get(2))
            elif cmd == 2:
                self.write(3, self.get(1) * self.get(2))
            elif cmd == 3:
                self.write(1, input)
            elif cmd == 4:
                output = self.get(1)
                self.IP += 2
                return output
            elif cmd == 5:
                self.IP = self.get(2) if self.get(1) else self.IP + 3
            elif cmd == 6:
                self.IP = self.get(2) if not self.get(1) else self.IP + 3
            elif cmd == 7:
                self.write(3, self.get(1) < self.get(2))
            elif cmd == 8:
                self.write(3, self.get(1) == self.get(2))
            else:
                exit(f"UNKNOWN OPCODE: {self.data[self.IP]}, pos {self.IP} ")

            self.IP += ADV[cmd]

        return 0

    @property
    def running(self):
        return self.data[self.IP] != 99

    def get(self, node):
        if (self.data[self.IP] // (10**(node + 1))) % 10:
            return self.data[self.IP + node]                # Immediate mode
        else:
            return self.data[self.data[self.IP + node]]     # Position mode

    def write(self, node, val):
        self.data[self.data[self.IP + node]] = val


nums = open('input07.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums2 = list(nums)


def part1():
    max_output = 0
    for phases in permutations([0, 1, 2, 3, 4]):
        amplifiers = [Machine(nums, phase) for phase in phases]
        out_in = 0
        for amplify in amplifiers:
            out_in = amplify.run(out_in)
        max_output = max(max_output, out_in)
    return max_output


def part2():
    max_output = 0
    for phases in permutations([5, 6, 7, 8, 9]):
        amplifiers = [Machine(nums, phase) for phase in phases]
        out_in = 0
        while amplifiers[0].running:
            for amplify in amplifiers:
                out_in = amplify.run(out_in)
                max_output = max(max_output, out_in)
    return max_output


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
