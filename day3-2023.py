filename = "readfile"

with open(filename) as f:
    lines = f.readlines()

for x in range(len(lines)):
    lines[x] = lines[x][:len(lines[x])-1]


def part1(stuff):
    numbers = []
    for line in range(len(stuff)):
        i = 0
        while i < len(stuff[line]):
            if stuff[line][i] in "0123456789":
                start = i
                while i < len(stuff[line]) and stuff[line][i] in "0123456789":
                    i += 1
                end = i
                check = [(i, j) for i in range(start-1, end+1) for j in range(line-1, line+2)]
                for coordinate in check:
                    try:
                        if stuff[coordinate[1]][coordinate[0]] not in "0123456789.":
                            numbers.append(int(stuff[line][start:end]))
                            break
                    except IndexError:
                        pass
            else:
                i += 1
    return sum(numbers)


def part2(stuff):
    numbers = []
    for line in range(len(stuff)):
        for i in range(len(stuff[line])):
            if stuff[line][i] == "*":
                gates = []
                if line == 0:
                    pass
                else:
                    j = i-1
                    while j < i+2:
                        if stuff[line-1][j] in "0123456789":
                            middle = j
                            while stuff[line-1][j] in "0123456789" and j >= 0:
                                j -= 1
                            start = j+1
                            j = middle
                            while j < len(stuff[line+1]) and stuff[line-1][j] in "0123456789":
                                j += 1
                            gates.append(int(stuff[line-1][start:j]))
                        j += 1
                if line == len(stuff) - 1:
                    pass
                else:
                    j = i - 1
                    while j < i + 2:
                        if stuff[line + 1][j] in "0123456789":
                            middle = j
                            while stuff[line + 1][j] in "0123456789" and j >= 0:
                                j -= 1
                            start = j+1
                            j = middle
                            while j < len(stuff[line+1]) and stuff[line+1][j] in "0123456789":
                                j += 1
                            gates.append(int(stuff[line + 1][start:j]))
                        j += 1
                if i == 0:
                    pass
                elif stuff[line][i-1] in "0123456789":
                    j = i-1
                    while stuff[line][j] in "0123456789" and j >= 0:
                        j -= 1
                    start = j+1
                    gates.append(int(stuff[line][start:i]))
                if i == len(stuff[i]) - 1:
                    pass
                elif stuff[line][i+1] in "0123456789":
                    j = i + 1
                    while stuff[line][j] in "0123456789" and j >= 0:
                        j += 1
                    gates.append(int(stuff[line][i+1:j]))
                if len(gates) == 2:
                    numbers.append(gates[0]*gates[1])
    return sum(numbers)


print(part2(lines))
