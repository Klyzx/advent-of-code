tottime = 2503
valspeed = [27, 22, 11, 28, 4, 14, 3, 18, 18]
valtime = [5, 2, 5, 5, 16, 3, 21, 6, 5]
valrest = [132, 41, 48, 134, 55, 38, 40, 103, 84]
valpoints = [0, 0, 0, 0, 0, 0, 0, 0, 0]
valdist = [0, 0, 0, 0, 0, 0, 0, 0, 0]
totdist = []

def reindeer(rest, time, speed, tottime=2503):
    distance = 0
    for i in range(1, tottime + 1):
        if (i % (rest + time) >= 1) and (i % (rest + time) <= time):
            distance += speed
    return distance

def reindeer2(rest, time, speed, now, reindeernum):
    if (now % (rest + time) >= 1) and (now % (rest + time) <= time):
        valdist[reindeernum] += speed

def pointcalc():
    for i in range(1, tottime + 1):
        for j in range(0, 9):
            reindeer2(valrest[j], valtime[j], valspeed[j], i, j)
        for k in range(0, 9):
            if valdist[k] == max(valdist):
                valpoints[k] += 1
    return(max(valpoints))

def olympics1():
    for i in range(0, 9):
        totdist.append(reindeer(valrest[i], valtime[i], valspeed[i]))
    return(max(totdist))

print(olympics1())
print(pointcalc())
