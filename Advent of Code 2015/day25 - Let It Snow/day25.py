code = 20151125                                 # Initial code value
grow = 2947                                     # Goal row [2947]
gcol = 3029                                     # Goal column [3029]
rnow = 1
cnow = 1

while(True):
    if rnow == grow and cnow == gcol:
        break
    code = ((code*252533) % 33554393)
    rnow -= 1
    cnow += 1
    if rnow == 0:
        rnow = cnow
        cnow = 1

print(code)
