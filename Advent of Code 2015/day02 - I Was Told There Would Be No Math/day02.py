totalpaper = 0
ribbon = 0

f = open("input02.txt")
for line in f:
    length, width, height = line.split('x')  #take list of inputs, split at x
    length = int(length)  #take each string and make them integers
    width = int(width)
    height = int(height)
    list = [length, width, height]
    list.sort()
    totalpaper += 2 * (length * height + length * width +
                       width * height) + list[0] * list[1]
    ribbon += 2 * (list[0] + list[1]) + length * width * height
print('Total square feet of wrapping paper: ', totalpaper)
print('Total ribbon length: ', ribbon)
