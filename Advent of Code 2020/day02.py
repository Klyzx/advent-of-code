import re


with open("inputs/02.in", "r") as file:
    data = list(file)


def part1(arr):
    valid = 0
    for line in arr:
        password = re.split("-| |: ", line.strip())
        n = password[3].count(password[2])
        if int(password[0]) <= n and n <= int(password[1]):
            valid += 1
    return valid


def part2(arr):
    valid = 0
    for line in arr:
        password = re.split("-| |: ", line.strip())
        word = password[3]
        valid += (word[int(password[0]) - 1] == password[2]) ^ \
                 (word[int(password[1]) - 1] == password[2])
    return valid


print(part1(data))
print(part2(data))
