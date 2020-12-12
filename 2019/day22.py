shuffles = open("inputs/22.in")
cards = list(range(10))
original = list(cards)
cycle = 1

while True:
    print(f"Cycle {cycle}")
    for line in shuffles:
        line = line[:-1].split()
        if line[0] == "cut":
            cut = int(line[1])
            cards = cards[cut:] + cards[:cut]
        elif line[2] == "new":
            cards.reverse()
        elif line[2] == "increment":
            inc = int(line[3])
            newcards = [0] * len(cards)
            for i in range(len(cards)):
                newcards[i * inc % len(cards)] = cards[i]
            cards = newcards
    shuffles.seek(0, 0)
    if cards == original:
        print(f"Cycle found of length: {cycle}")
        break
    cycle += 1


print(cards)
