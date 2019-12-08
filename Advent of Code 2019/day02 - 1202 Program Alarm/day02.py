ADV = {1: 4, 2: 4, 3: 2, 4: 0, 5: 0, 6: 0, 7: 4, 8: 4}


class Machine:
    def __init__(self, data):
        self.data = list(data)
        self.IP = 0

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


nums = open('input02.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums2 = list(nums)
backup = list(nums)

nums[1] = 12
nums[2] = 2

computer = Machine(nums)

computer.run()
print(computer.data[0])


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


part2()
