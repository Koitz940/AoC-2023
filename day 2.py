import numpy

filename = "calibration_document"

with open(filename) as f:
    lines = f.readlines()


def ballscheck(red_balls, blue_balls, green_balls, iden):
    for amount in red_balls:
        if amount > 12:
            return 0
    for amount in blue_balls:
        if amount > 14:
            return 0
    for amount in green_balls:
        if amount > 13:
            return 0
    return iden


def part1(self):
    id_stored = []
    iden = 1
    for line in self:
        red_balls = []
        blue_balls = []
        green_balls = []
        splitline = line.split()
        for i in range(len(splitline)):
            if splitline[i] == "blue," or splitline[i] == "blue;" or splitline[i] == "blue":
                blue_balls = blue_balls + [int(splitline[i-1])]
            if splitline[i] == "red," or splitline[i] == "red;" or splitline[i] == "red":
                red_balls = red_balls + [int(splitline[i-1])]
            if splitline[i] == "green," or splitline[i] == "green" or splitline[i] == "green;":
                green_balls = green_balls + [int(splitline[i-1])]

        id_stored.append(ballscheck(red_balls, blue_balls, green_balls, iden))
        sum(id_stored)
        iden += 1
    return sum(id_stored)


def colorpower(red, green, blue):
    colors = [red, green, blue]
    factors = []
    for color in colors:
        color.sort()
        factors += [color[-1]]
    return numpy.prod(factors)


def part2(self):
    powers_stored = []
    for line in self:
        red_balls = []
        blue_balls = []
        green_balls = []
        splitline = line.split()
        for i in range(len(splitline)):
            if splitline[i] == "blue," or splitline[i] == "blue;" or splitline[i] == "blue":
                blue_balls = blue_balls + [int(splitline[i - 1])]
            if splitline[i] == "red," or splitline[i] == "red;" or splitline[i] == "red":
                red_balls = red_balls + [int(splitline[i - 1])]
            if splitline[i] == "green," or splitline[i] == "green" or splitline[i] == "green;":
                green_balls = green_balls + [int(splitline[i - 1])]
        powers_stored += [colorpower(red_balls, green_balls, blue_balls)]
    return sum(powers_stored)


print(part1(lines))
print(part2(lines))
