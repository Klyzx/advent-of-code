with open("inputs/04.in", "r") as file:
    data = file.read().split('\n\n')
for i in range(len(data)):
    data[i] = data[i].replace('\n', ' ').strip()

passportInformation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyeColor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def passportCheck(passport):
    requiredFields = 0
    requiredFields = 0
    for key in passportInformation:
        if key in passport:
            requiredFields += 1
    if requiredFields == 7:
        return True
    return False


def passportStrict(passport):
    hgt = int(str(0) + passport.get("hgt")[:-2])
    cmin = passport.get("hgt")[-2:]
    if not 1920 <= int(passport.get("byr")) <= 2002:
        return False
    if not 2010 <= int(passport.get("iyr")) <= 2020:
        return False
    if not 2020 <= int(passport.get("eyr")) <= 2030:
        return False
    if passport.get("ecl") not in eyeColor:
        return False
    if len(passport.get("pid")) != 9:
        return False
    if len(passport.get("hcl")) != 7:
        return False
    if cmin == "cm":
        if not 150 <= hgt <= 193:
            return False
    elif cmin == "in":
        if not 59 <= hgt <= 76:
            return False
    else:
        return False
    return True


validPassports = 0
strictPassports = 0

for i in range(len(data)):
    passportData = dict(x.split(":") for x in data[i].split(" "))
    passportValid = passportCheck(passportData)
    validPassports += passportValid
    if passportValid:
        passportValid = passportStrict(passportData)
        strictPassports += passportValid

print(validPassports)
print(strictPassports)
