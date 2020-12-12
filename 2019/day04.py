from itertools import groupby


def repetitions(num):
    string = ""
    grouped_data = groupby(str(num))
    for _, grp in grouped_data:
        string += str(len(list(grp)))
    return string


def checker(num):
    repeat = repetitions(num)
    if [x for x in str(num)] != sorted(str(num)):
        return False
    for x in repeat:
        if int(x) >= 2:
            return True
    return False


def checker2(num):
    repeat = repetitions(num)
    for x in repeat:
        if int(x) == 2:
            return True
    return False


minr = 245318
maxr = 765747
valid1 = 0
valid2 = 0

for x in range(minr, maxr + 1):
    if checker(x):
        valid1 += 1
        if checker2(x):
            valid2 += 1

print(valid1, valid2)
