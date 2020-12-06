with open("inputs/05.in", "r") as file:
    data = file.read().splitlines()


def seatID(boardpass):
    row = boardpass[:7]
    row = int(row.replace('B', '1').replace('F', '0'), 2)
    column = boardpass[-3:]
    column = int(column.replace('R', '1').replace('L', '0'), 2)
    return row * 8 + column


highest = 0
allseats = []
for i in range(len(data)):
    currentSeat = seatID(data[i])
    highest = currentSeat if currentSeat > highest else highest
    allseats.append(currentSeat)

print(highest)

for i in range(min(allseats), max(allseats)):
    if i not in allseats:
        print(i)
