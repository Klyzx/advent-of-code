from sympy.ntheory.modular import crt


with open("inputs/13.in", "r") as file:
    timestamp = int(file.readline())
    buses = file.readline().split(',')

minwait = (0, timestamp)
for bus in buses:
    if bus != 'x':
        bus = int(bus)
        time = 0
        while time < timestamp:
            time += bus
        if time - timestamp < minwait[1]:
            minwait = (bus, time - timestamp)

residue = []
modulus = []
for index, item in enumerate(buses):
    if item == "x":
        continue
    residue.append(int(item) - index)
    modulus.append(int(item))


print(minwait[0]*minwait[1])
print(crt(modulus, residue)[0])
