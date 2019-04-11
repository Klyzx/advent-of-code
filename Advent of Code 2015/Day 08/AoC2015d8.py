stringliteral = 0
stringmemory = 0
stringnew = 0

def sizeliteral(string):
    return len(string)

def sizememory(string):
    return len(eval(string))

def newstring(string):
    string = string.replace("\\", "\\\\")
    string = string.replace("\"", "\\\"")

    print(string)
    return (len(string) + 2)

with open('../inputs.txt') as file:
    for line in file:
        line = line.rstrip()
        stringliteral += sizeliteral(line)
        stringmemory  += sizememory(line)
        stringnew += newstring(line)


print("Literal - Memory:   ", stringliteral - stringmemory)
print("Literal - New:      ", stringnew - stringliteral)
print("String literal:     ", stringliteral)
print("String memory:      ", stringmemory)
print("String new:         ", stringnew)