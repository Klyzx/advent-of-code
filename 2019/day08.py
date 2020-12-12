from re import findall
import matplotlib.pyplot as plt
wide = 25
tall = 6

split = wide * tall
layers = findall('.'*split, open('inputs/08.in').read())


def part1():
    fewest0 = split
    onetwo = 0
    for layer in layers:
        if layer.count('0') < fewest0:
            onetwo = layer.count('1') * layer.count('2')
            fewest0 = layer.count('0')
    return onetwo


def divide(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def part2():
    image = [2]*split
    for layer in layers:
        for char in range(len(layer)):
            if image[char] == 2:
                image[char] = int(layer[char])
    image = list(divide(image, 25))
    plt.set_cmap('binary')
    plt.axis('off')
    plt.imshow(image)


print(part1())
part2()
