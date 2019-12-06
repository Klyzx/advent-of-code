floor = 0
position = 0
positiontrigger = False

with open("input01.txt") as f:
    while True:
        char = f.read(1)
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print('The final floor is: ', floor)
            break
        position += 1
        if floor < 0 and positiontrigger is False:
            print('The position Santa goes into the basement: ', position)
            positiontrigger = True
