ADV = {1: 4, 2: 4, 3: 2, 4: 0, 5: 0, 6: 0, 7: 4, 8: 4}


class Machine:
    def __init__(self, data, ID):
        self.data = list(data)
        self.IP = 0
        self.write(1, ID)
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


nums = open('input05.txt').read().split(',')
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums2 = list(nums)

machine1 = Machine(nums, 1)
machine2 = Machine(nums, 5)
out1 = 0
out2 = 0

while out1 == 0:
    out1 = machine1.run()
while out2 == 0:
    out2 = machine2.run()

print(f"Part 1: {out1}")
print(f"Part 2: {out2}")
