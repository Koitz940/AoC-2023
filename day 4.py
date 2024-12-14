filename = "calibration_document"

with open(filename) as f:
    lines = f.readlines()


def part1(self):
    answer = 0
    for line in self:
        x = 0
        splitline = line.split()
        middle = splitline.index("|")
        for number in splitline[2:middle]:
            for win in splitline[middle + 1:]:
                if int(number) == int(win):
                    x += 1
                    break
        if x != 0:
            answer += 2 ** (x - 1)
    return answer


def part2(line):
    x = 0
    splitline = line.split()
    middle = splitline.index("|")
    for number in splitline[2:middle]:
        for win in splitline[middle + 1:]:
            if int(number) == int(win):
                x += 1
                break
    if x == 0:
        return 1
    elif lines.index(line) + x < len(lines):
        return 1 + sum(map(part2, lines[lines.index(line)+1:lines.index(line)+1+x]))
    else:
        return 1 + sum(map(part2, lines[lines.index(line):len(lines)-1]))


print(sum(map(part2, lines)))
