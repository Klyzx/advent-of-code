wires = []  # List of wires
signl = []  # List of signals
instr = []  # List of instructions
delet = []

with open("input07.txt") as f:
    count = 0
    for line in f:
        instr.append(line[:-1])  # Remove new line character
        count += 1


def stringsplit(string):
    """
    Splits a string into two parts by ' -> '
    e.g. '123 -> x' becomes '123' and 'x'

    Parameters
    ----------
    string : string
        String to be converted into smaller parts

    """

    global parta
    global partb

    parta, partb = string.split(" -> ")
    parta = parta.split()


def removeinstr(deleted):
    """
    Removes numbers from instr and reduces count as well

    Parameters
    ----------
    deleted : list
        The list of all numbers that need to be removed from the instructions
        after having been performed

    """
    global count
    deleted.sort(reverse=True)
    for i in deleted:
        del instr[i]
        count -= 1
    delet.clear()


def initialize():
    """
    This function adds all of the wires with a given value in input to the
    wires list
    """
    for i in range(0, count):
        stringsplit(instr[i])
        try:
            signl.append(int(parta[0]))
            wires.append(partb)
            delet.append(i)
        except:
            pass
    removeinstr(delet)


def therest():
    while count > 0:
        for i in range(0, count):
            stringsplit(instr[i])
            if len(parta) == 1:
                if parta[0] in wires:
                    signl.append(signl[wires.index(parta[0])])
                    wires.append(partb)
                    delet.append(i)
                continue
            elif parta[1] == "AND":
                try:
                    signl.append(signl[wires.index(parta[0])]
                                 & signl[wires.index(parta[2])])
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                try:
                    signl.append(signl[wires.index(parta[0])] & int(parta[2]))
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                try:
                    signl.append(signl[wires.index(parta[2])] & int(parta[0]))
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                continue
            elif parta[1] == "OR":
                try:
                    signl.append(signl[wires.index(parta[0])]
                                 | signl[wires.index(parta[2])])
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                try:
                    signl.append(signl[wires.index(parta[0])] | int(parta[2]))
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                try:
                    signl.append(signl[wires.index(parta[2])] | int(parta[0]))
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                continue
            elif (parta[0] in wires) and (parta[1] == "LSHIFT"):
                try:
                    signl.append(signl[wires.index(parta[0])] << int(parta[2]))
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                continue
            elif (parta[0] in wires) and (parta[1] == "RSHIFT"):
                try:
                    signl.append(signl[wires.index(parta[0])] >> int(parta[2]))
                    wires.append(partb)
                    delet.append(i)
                    continue
                except:
                    pass
                continue
            elif (parta[0] == "NOT") and (parta[1] in wires):
                signl.append(65535 - signl[wires.index(parta[1])])
                wires.append(partb)
                delet.append(i)
                continue
        removeinstr(delet)


initialize()
therest()
print(instr)
print(wires)
print(signl)
print(signl[wires.index("a")])
