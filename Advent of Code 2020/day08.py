with open("inputs/08.in", "r") as file:
    bootCode = file.read().splitlines()

accumulator = 0
ip = 0


def runInstruction(instruction):
    global accumulator
    global ip
    instruction = instruction.split(' ')
    if instruction[0] == "acc":
        accumulator += int(instruction[1])
        ip += 1
    elif instruction[0] == "jmp":
        ip += int(instruction[1])
    else:
        ip += 1


def part1(code):
    instructionsVisited = set()
    while ip not in instructionsVisited:
        instructionsVisited.add(ip)
        runInstruction(code[ip])
    return accumulator


def part2(code):
    global accumulator
    global ip
    for i in range(len(code)):
        # Change instruction if it is nop / jmp
        tempCode = list(code)
        changeInstruction = tempCode[i].split(' ')
        if changeInstruction[0] == "nop":
            tempCode[i] = "jmp" + changeInstruction[1]
        elif changeInstruction[0] == "jmp":
            tempCode[i] = "nop" + changeInstruction[1]
        else:
            continue

        # Attempt to run, if it gets stuck in infinite loop quit
        accumulator = 0
        ip = 0
        instructionsVisited = set()
        while ip not in instructionsVisited:
            if ip not in range(len(tempCode)):
                return accumulator
            instructionsVisited.add(ip)
            runInstruction(tempCode[ip])


print(part1(bootCode))
print(part2(bootCode))
