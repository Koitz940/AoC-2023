filename = "calibration_document"

with open(filename) as f:
    lines = f.readlines()


def create(file):
    to_do = []
    for line in file:
        sequence = line.split()
        wanted = list(map(int, sequence))
        to_do.append(wanted)
    return to_do


def part1(line):
    previous = line[-1]
    nextline = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    for x in range(len(line) - 1):
        if max(nextline) == 0 and min(nextline) == 0:
            break
        else:
            previous += nextline[-1]
            nextline = [nextline[i + 1] - nextline[i] for i in range(len(nextline) - 1)]
    return previous


def part2(line):
    previous = line[0]
    symbol = 1
    nextline = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    for x in range(len(line)-1):
        if max(nextline) == 0 and min(nextline) == 0:
            break
        else:
            previous += nextline[0] * (-1)**symbol
            nextline = [nextline[i + 1] - nextline[i] for i in range(len(nextline) - 1)]
            symbol += 1
    return previous


print(sum(map(part1, create(lines))))
