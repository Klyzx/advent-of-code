values = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]
names = ["children", "cats", "samoyeds", "pomeranians", "akitas",
         "vizslas", "goldfish", "trees", "cars", "perfumes"]


def checks(lista):
    global correct
    for i in range(0, 10):
        if ((lista[2] == names[i] and int(lista[3]) == values[i])
                or (lista[4] == names[i] and int(lista[5]) == values[i])
                or (lista[6] == names[i] and int(lista[7]) == values[i])):
            correct += 1


values2 = [3, 2, 0, 0, 2, 1]
names2 = ["children", "samoyeds", "akitas", "vizslas", "cars", "perfumes"]


def checks2(lista):
    global correct
    for i in range(0, 6):
        if ((lista[2] == names[i] and int(lista[3]) == values[i])
                or (lista[4] == names[i] and int(lista[5]) == values[i])
                or (lista[6] == names[i] and int(lista[7]) == values[i])):
            correct += 1
    if ((lista[2] == "cats" and int(lista[3]) > 7)
            or (lista[4] == "cats" and int(lista[5]) > 7)
            or (lista[6] == "cats" and int(lista[7]) > 7)):
        correct += 1
    if ((lista[2] == "trees" and int(lista[3]) > 3)
            or (lista[4] == "trees" and int(lista[5]) > 3)
            or (lista[6] == "trees" and int(lista[7]) > 3)):
        correct += 1
    if ((lista[2] == "pomeranians" and int(lista[3]) < 3)
            or (lista[4] == "pomeranians" and int(lista[5]) < 3)
            or (lista[6] == "pomeranians" and int(lista[7]) < 3)):
        correct += 1
    if ((lista[2] == "goldfish" and int(lista[3]) < 5)
            or (lista[4] == "goldfish" and int(lista[5]) < 5)
            or (lista[6] == "goldfish" and int(lista[7]) < 5)):
        correct += 1


with open("input16.txt") as f:
    for line in f:
        correct = 0
        line = line.replace(',', ' ').replace(':', ' ').split()
        checks(line)
        if correct == 3:
            print("Sue: ", line[1])
        correct = 0
        checks2(line)
        if correct == 3:
            print("Real Sue: ", line[1])
