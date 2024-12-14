numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}
filename = "readfile"

with open(filename) as f:
    lines = f.readlines()


def part1(stuff):
    elements = []
    for line in stuff:
        for i in line:
            if i.isnumeric():
                first = i
                break
        for i in line[::-1]:
            if i.isnumeric():
                second = i
        elements.append(10*int(first) + int(second))
    return sum(elements)


def part2(stuff):
    elements = []
    for line in stuff:
        line = line[:len(line) - 1]
        i = 0
        a = None
        while a is None:
            j = 1
            while j <= len(line):
                if line[i:i + j] in numbers:
                    a = numbers[line[i:i + j]]
                    break
                j += 1
            i += 1
        i = len(line)
        b = None
        while b is None:
            j = 1
            while j <= len(line):
                if line[i - j:i] in numbers:
                    b = numbers[line[i - j:i]]
                    break
                j += 1
            i -= 1
        elements.append(int(10 * a + b))
    return sum(elements)
