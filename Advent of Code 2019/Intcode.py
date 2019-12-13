from sys import exit
from collections import defaultdict
ADV = {1: 4, 2: 4, 3: 2, 4: 0, 5: 0, 6: 0, 7: 4, 8: 4, 9: 2}
OPC = {1: "ADD",
       2: "MUL",
       3: "INP",
       4: "OUT",
       5: "JNZ",
       6: "JZ",
       7: "LESS",
       8: "EQL",
       9: "BASE"}


class Machine:
    def __init__(self, data, input=None, debug=False):
        self.data = defaultdict(int, enumerate(data))
        self.IP = 0
        self.REL = 0
        self.DEBUG = debug
        self.INS = 0
        if input is not None:
            self.write(1, input)
            self.IP += 2

    def run(self, input=None):
        while self.running:
            cmd = self.data[self.IP] % 100
            if self.DEBUG:
                self.INS += 1
                print(f"INS: {self.INS}, CMD: {self.data[self.IP]} {OPC[cmd]}")

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
            elif cmd == 9:
                self.REL += self.get(1)
            else:
                exit(f"UNKNOWN OPCODE: {self.data[self.IP]}, pos {self.IP} ")

            self.IP += ADV[cmd]
        return 0

    @property
    def running(self):
        return self.data[self.IP] != 99

    def get(self, node):
        if (self.data[self.IP] // (10**(node + 1))) % 10 == 1:
            return self.data[self.IP + node]
        elif (self.data[self.IP] // (10**(node + 1))) % 10 == 2:
            return self.data[self.data[self.IP + node] + self.REL]
        else:
            return self.data[self.data[self.IP + node]]

    def write(self, node, val):
        if (self.data[self.IP] // (10**(node + 1))) % 10 == 2:
            self.data[self.data[self.IP + node] + self.REL] = val
        else:
            self.data[self.data[self.IP + node]] = val
