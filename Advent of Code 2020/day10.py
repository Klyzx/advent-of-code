from collections import defaultdict


with open("inputs/10.in", "r") as file:
    data = list(map(int, file))


def part1(voltages):
    diff_list = []
    for x, y in zip(voltages[0:], voltages[1:]):
        diff_list.append(y-x)
    print(diff_list.count(1)*diff_list.count(3))


def validAdapter(voltage, adapterList, adaptersChecked):
    valid = 0
    if voltage == 0:
        return 1
    for i in range(1, 4):
        if voltage - i in adapterList:
            if adaptersChecked[voltage - i]:
                valid += adaptersChecked[voltage - i]
                continue
            valid += validAdapter(voltage - i, adapterList, adaptersChecked)
        adaptersChecked[voltage] = valid
    return valid


data.append(0)
data.append(max(data)+3)
data.sort()
adapterDict = defaultdict(int)

part1(data)
validAdapter(max(data), data, adapterDict)
