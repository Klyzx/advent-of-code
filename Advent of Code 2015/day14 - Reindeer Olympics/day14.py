tottime = 2503
valspeed  = [ 22,   8,  18,  25,  11,  21, 18, 20,   7]
valtime   = [  8,  17,   6,   6,  12,   6,  3,  4,  20]
valrest   = [165, 114, 103, 145, 125, 121, 50, 75, 119]
valpoints = [  0,   0,   0,   0,   0,   0,  0,  0,   0]
valdist   = [  0,   0,   0,   0,   0,   0,  0,  0,   0]
totdist   = []

def reindeer(rest, time, speed, tottime = 2503):
    distance = 0
    for i in range(1, tottime + 1):
        if (i % (rest+time) >= 1) and (i % (rest+time) <= time):
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
    print(max(valpoints))

def olympics1():
    for i in range(0, 9):
        totdist.append(reindeer(valrest[i], valtime[i], valspeed[i]))
    print(max(totdist))

olympics1()
pointcalc()
