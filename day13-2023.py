import time

start = time.time()

filename = "readfile"

with open(filename) as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()


records = []
index = 0
for i in range(len(lines)):
    if lines[i] == "":
        records.append(lines[index:i])
        index = i+1
records.append(lines[index:])

def transpose(thing):
    rows = len(thing)
    cols = len(thing[0])
    return [[thing[a][b] for a in range(rows)] for b in range(cols)]

def part1(stuff):
    def check(data: list[list], mult: int) -> int:
        for a in range(1, len(data)):
            match a < len(data)//2:
                case True:
                    if all(data[a-j-1] == data[a+j] for j in range(a)):
                        return mult * a
                case False:
                    if all(data[a - j - 1] == data[a + j] for j in range(len(data) - a)):
                        return mult * a

    def findmirror(data):
        rows = check(data, 100)
        if rows is None:
            data = transpose(data)
            return check(data, 1)
        return rows

    return sum(list(map(findmirror, stuff)))


def part2(stuff):
    def check(data, mult):
        for a in range(1, len(data)):
            if data[a] == data[a-1]:
                match a < len(data)//2:
                    case True:
                        pairs = [(data[a-j-1], data[a+j]) for j in range(a)]
                        single_off_count = [z for z in pairs if
                                            [z[0][x] == z[1][x] for x in range(len(z[0]))].count(False) == 1]
                        multiple_off_count = [z for z in pairs if
                                              [z[0][x] == z[1][x] for x in range(len(z[0]))].count(False) > 1]
                        if len(single_off_count) == 1 and len(multiple_off_count) == 0:
                            return mult * a
                    case False:
                        pairs = [(data[a - j - 1], data[a + j]) for j in range(len(data)-a)]
                        single_off_count = [z for z in pairs if [z[0][x] == z[1][x] for x in range(len(z[0]))].count(False) == 1]
                        multiple_off_count = [z for z in pairs if [z[0][x] == z[1][x] for x in range(len(z[0]))].count(False) > 1]
                        if len(single_off_count) == 1 and len(multiple_off_count) == 0:
                            return mult * a
            elif [data[a][z] == data[a-1][z] for z in range(len(data[a]))].count(False) == 1:
                match a < len(data) // 2:
                    case True:
                        if all(data[a - j - 1] == data[a + j] for j in range(1,a)):
                            return mult * a
                    case False:
                        if all(data[a - j - 1] == data[a + j] for j in range(1, len(data) - a)):
                            return mult * a

    def notfindmirror(data: list[list]) -> int:
        rows = check(data, 100)
        if rows is None:
            return check(transpose(data), 1)
        return rows
    return sum(list(map(notfindmirror, stuff)))


print(part2(records), part1(records))

end = time.time()
print(end-start)
