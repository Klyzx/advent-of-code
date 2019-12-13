class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vels = [0, 0, 0]

    def compare(self, other):
        for i in range(len(self.pos)):
            if self.pos[i] > other.pos[i]:
                self.vels[i] -= 1
                other.vels[i] += 1
            elif self.pos[i] < other.pos[i]:
                self.vels[i] += 1
                other.vels[i] -= 1

    def move(self):
        for i in range(len(self.vels)):
            self.pos[i] += self.vels[i]


def run(steps, pt2=False):
    for step in range(steps):
        a.compare(b)
        a.compare(c)
        a.compare(d)
        b.compare(c)
        b.compare(d)
        c.compare(d)

        for moon in [a, b, c, d]:
            moon.move()
        for moon in [a, b, c, d]:
            print(moon.pos, moon.vels)


a = Moon(14, 2, 8)
b = Moon(7, 4, 10)
c = Moon(1, 17, 16)
d = Moon(-4, -1, 1)

run(1000)

energy = 0
for moon in [a, b, c, d]:
    pot = 0
    kin = 0
    for i in range(3):
        pot += abs(moon.pos[i])
        kin += abs(moon.vels[i])
    energy += pot*kin

print(energy)
