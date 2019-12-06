santax = 0
santay = 0
robox = 0
roboy = 0
isrobotactive = 0  # set to 1 to activate the santa robot
santavsroboturn = 0
houselist = {}
uniquehouse = 0

DX = {'<': -1, '>': 1, '^': 0, 'v': 0}
DY = {'<': 0, '>': 0, '^': 1, 'v': -1}

with open('input03.txt') as f:
    while 1:
        direction = f.read(1)
        if santavsroboturn == 0 and direction != '\n':
            santax += DX[direction]
            santay += DY[direction]
            if isrobotactive == 1:
                santavsroboturn = 1
            if (santax, santay) not in houselist:
                houselist[(santax, santay)] = uniquehouse
                uniquehouse += 1
        else:
            if direction == '\n':
                break
            robox += DX[direction]
            roboy += DY[direction]
            santavsroboturn = 0
            if (robox, roboy) not in houselist:
                houselist[(robox, roboy)] = uniquehouse
                uniquehouse += 1

print('The total amount of unique houses is: ', uniquehouse)
