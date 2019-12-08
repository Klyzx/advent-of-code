parens = open('input01.txt').read()
print(f"Last: {parens.count('(') - parens.count(')')}")
opens = 0
close = 0
for i in parens:
    if i == '(':
        opens += 1
    else:
        close += 1
    if opens < close:
        print(f"First basement: {opens+close}")
        break
