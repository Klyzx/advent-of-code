evilstrings = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
characterposition = 0
amountofnicestrings = 0
stringnicenesscounter = 0

with open('input05.txt') as f:
    for line in f:
        vowelsinword = 0  # Set these variables to 0 at the start of every line
        readlineposition = 0
        stringnicenesscounter = 0
        for characterposition in line:  # count each letter in the line
            if characterposition in vowels:  # if the letter is a vowel then add 1 to vowels
                vowelsinword += 1
        if vowelsinword >= 3:
            stringnicenesscounter += 1
        if 'xy' in line:
            stringnicenesscounter = 0
        if 'pq' in line:
            stringnicenesscounter = 0
        if 'cd' in line:
            stringnicenesscounter = 0
        if 'ab' in line:
            stringnicenesscounter = 0
        for characterposition in line:
            if characterposition == line[readlineposition + 1]:
                stringnicenesscounter += 1
                break
            readlineposition += 1
            if readlineposition + 1 == len(line):
                break
        if stringnicenesscounter == 2:
            amountofnicestrings += 1
print("Amount of nice strings 1: ", amountofnicestrings)

amountofnicestrings = 0
with open('input05.txt') as f:
    for line in f:
        stringnicenesscounter = 0
        currentstring = list(line)
        currentstring.pop()
        length = len(line)
        length -= 1
        i = 0
        while i <= length - 3:
            if currentstring[i] == currentstring[
                    i +
                    2]:  #check each position in the word, if it matches the one two spots later then it matches and ends
                stringnicenesscounter += 1
                break
            i += 1
        i = 0
        r = 2
        while i + 3 <= length:
            while i + r + 1 <= length:
                part = currentstring[i:i + 2]
                if part == currentstring[r + i:r + i + 2]:
                    stringnicenesscounter += 1
                    i = 100
                    break
                r += 1
            i += 1
            r = 2
        if stringnicenesscounter == 2:
            amountofnicestrings += 1

print("Amount of nice strings 2: ", amountofnicestrings)
