with open("inputs/06.in", "r") as file:
    data = file.read().split('\n\n')
for i in range(len(data)):
    data[i] = data[i].strip()


anyone = 0
everyone = 0
for i in range(len(data)):
    anyone += len(set(data[i].replace('\n', '')))
    alls = data[i].split('\n')
    sets = set(alls[0])
    for i in range(len(alls)):
        sets = sets.intersection(set(alls[i]))
    everyone += len(sets)

print(anyone)
print(everyone)
