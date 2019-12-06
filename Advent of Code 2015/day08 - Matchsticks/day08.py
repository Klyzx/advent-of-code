stringliteral = 0
stringmemory = 0
stringnew = 0


def newstring(string):
    string = string.replace("\\", "\\\\").replace('"', '\\"')
    return len(string) + 2


with open("input08.txt") as f:
    for line in f:
        line = line.rstrip()
        stringliteral += len(line)
        stringmemory += len(eval(line))
        stringnew += newstring(line)

print("Literal - Memory:   ", stringliteral - stringmemory)
print("Literal - New:      ", stringnew - stringliteral)
print("String literal:     ", stringliteral)
print("String memory:      ", stringmemory)
print("String new:         ", stringnew)
