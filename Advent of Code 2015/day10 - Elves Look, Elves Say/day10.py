from itertools import groupby

number = "1113122113"


def newnumber(currentnum):
    string = ""
    grouped_data = groupby(number)
    for key, grp in grouped_data:
        string += str(len(list(grp)))
        string += key
    return string


for i in range(0, 40):
    number = newnumber(number)
number1 = number

for i in range(0, 10):
    number = newnumber(number)

print(len(number1))
print(len(number))
