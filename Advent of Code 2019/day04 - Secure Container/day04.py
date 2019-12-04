from itertools import groupby

def checker(num):
    consec = False
    incr = True
    num = str(num)
    for x in range(len(num) - 1):
        if num[x] == num[x + 1]:
            consec = True
        if num[x] > num[x + 1]:
            incr = False
    return consec and incr

def newnumber(currentnum):
    string = ""
    grouped_data = groupby(str(currentnum))
    for _, grp in grouped_data:
        string += str(len(list(grp)))
    return string

def checker2(num):
    blank = ""
    string = newnumber(num)
    for x in range(len(string)):
        blank += string[x]
    for x in blank:
        if int(x) == 2:
            return True
    return False

minr = 245318
maxr = 765747
valid1 = 0
valid2 = 0

for num in range(minr, maxr + 1):
    if checker(num):
        valid1 += 1
        if checker2(num):
            valid2 += 1

print(valid1, valid2)
