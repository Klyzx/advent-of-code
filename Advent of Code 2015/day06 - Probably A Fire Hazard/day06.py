import numpy

lightarray = numpy.zeros([1000, 1000], dtype="int")
with open("input06.txt") as f:
    for line in f:
        instruction = line.replace(",", " ").split()
        if instruction[1] == "on":
            x1 = int(instruction[2])
            y1 = int(instruction[3])
            x2 = int(instruction[5])
            y2 = int(instruction[6])
            currentx = x1
            currenty = y1
            topleft = (x1, y1)
            bottomright = (x2, y2)
            while currentx <= x2:
                while currenty <= y2:
                    lightarray[currentx, currenty] = 1
                    currenty += 1
                currenty = y1
                currentx += 1
        elif instruction[1] == "off":
            x1 = int(instruction[2])
            y1 = int(instruction[3])
            x2 = int(instruction[5])
            y2 = int(instruction[6])
            currentx = x1
            currenty = y1
            topleft = (x1, y1)
            bottomright = (x2, y2)
            while currentx <= x2:
                while currenty <= y2:
                    lightarray[currentx, currenty] = 0
                    currenty += 1
                currenty = y1
                currentx += 1
        else:
            x1 = int(instruction[1])
            y1 = int(instruction[2])
            x2 = int(instruction[4])
            y2 = int(instruction[5])
            currentx = x1
            currenty = y1
            topleft = (x1, y1)
            bottomright = (x2, y2)
            while currentx <= x2:
                while currenty <= y2:
                    if lightarray[currentx, currenty] == 0:
                        lightarray[currentx, currenty] = 1
                    else:
                        lightarray[currentx, currenty] = 0
                    currenty += 1
                currenty = y1
                currentx += 1
print("Lights on: ", numpy.count_nonzero(lightarray))

lightarray = numpy.zeros([1000, 1000], dtype="int")
with open("input06.txt") as f:
    for line in f:
        instruction = line.replace(",", " ").split()
        if instruction[1] == "on":
            x1 = int(instruction[2])
            y1 = int(instruction[3])
            x2 = int(instruction[5])
            y2 = int(instruction[6])
            currentx = x1
            currenty = y1
            topleft = (x1, y1)
            bottomright = (x2, y2)
            while currentx <= x2:
                while currenty <= y2:
                    lightarray[currentx, currenty] += 1
                    currenty += 1
                currenty = y1
                currentx += 1
        elif instruction[1] == "off":
            x1 = int(instruction[2])
            y1 = int(instruction[3])
            x2 = int(instruction[5])
            y2 = int(instruction[6])
            currentx = x1
            currenty = y1
            topleft = (x1, y1)
            bottomright = (x2, y2)
            while currentx <= x2:
                while currenty <= y2:
                    lightarray[currentx, currenty] -= 1
                    if lightarray[currentx, currenty] < 0:
                        lightarray[currentx, currenty] = 0
                    currenty += 1
                currenty = y1
                currentx += 1
        else:
            x1 = int(instruction[1])
            y1 = int(instruction[2])
            x2 = int(instruction[4])
            y2 = int(instruction[5])
            currentx = x1
            currenty = y1
            topleft = (x1, y1)
            bottomright = (x2, y2)
            while currentx <= x2:
                while currenty <= y2:
                    lightarray[currentx, currenty] += 2
                    currenty += 1
                currenty = y1
                currentx += 1

print("Total brightness: ", numpy.sum(lightarray))
