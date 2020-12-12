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
    """Intcode Computer implementation

    Parameters
    ----------
    data : list
        The program data of the computer
    inputs : list
        List of inputs for the computer (the default is []).
    old_input : int
        Old input method if first opcode is 3 (the default is None).
    debug : bool
        If true, prints out all instructions (the default is False).
    day : int
        This shouldn't need to exist but it's for day 25

    """

    def __init__(self, data, inputs=[], old_input=None, debug=False, day=None):
        self.data = defaultdict(int, enumerate(data))
        self.IP = 0
        self.REL = 0
        self.DEBUG = debug
        self.INS = 0
        self.INPUT = inputs
        self.DAY = day
        if old_input is not None:
            self.write(1, old_input)
            self.IP += 2

    def run(self, old_input=None):
        """Runs one loop of the computer until opcode 4 or computer halts

        Parameters
        ----------
        old_input : int
            Old input method, deprecated (the default is None).

        Returns
        -------
        int
            Returns integer on opcode 4

        """
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
                if old_input is None and self.DAY is None:
                    self.write(1, self.INPUT[0])
                    self.INPUT = self.INPUT[1:]
                elif self.DAY is None:
                    self.write(1, old_input)
                elif self.DAY == 25:
                    if self.INPUT == []:
                        inst = input()
                        inst += '\n'
                        self.INPUT = [ord(c) for c in inst]
                    self.write(1, self.INPUT[0])
                    self.INPUT = self.INPUT[1:]
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
        """Returns if computer is running

        Returns
        -------
        bool
            True if Intcode Computer hasn't reached opcode 99 yet

        """
        return self.data[self.IP] != 99

    def get(self, node):
        """Returns value of node

        Parameters
        ----------
        node : int
            Node to get value from in position, immediate, or relative mode

        Returns
        -------
        int
            Returns value of parameter

        """
        if (self.data[self.IP] // (10**(node + 1))) % 10 == 1:
            return self.data[self.IP + node]
        elif (self.data[self.IP] // (10**(node + 1))) % 10 == 2:
            return self.data[self.data[self.IP + node] + self.REL]
        else:
            return self.data[self.data[self.IP + node]]

    def write(self, node, val):
        """Writes val to node

        Parameters
        ----------
        node : int
            Node position to write to
        val : int
            Value to write at node

        """
        if (self.data[self.IP] // (10**(node + 1))) % 10 == 2:
            self.data[self.data[self.IP + node] + self.REL] = val
        else:
            self.data[self.data[self.IP + node]] = val

    def set_input(self, newinput):
        """Replaces the current input with newinput

        Parameters
        ----------
        newinput : list
            List of inputs to use with opcode 3

        """
        self.INPUT = newinput
