filename = "readfile"

with open(filename) as f:
    lines = f.readlines()


guide = {
    "|": [[[0, 1], [0, -1]], [[0, 1], [0, -1]]],
    "-": [[[1, 0], [-1, 0]], [[1, 0], [-1, 0]]],
    "L": [[[0, 1], [-1, 0]], [[1, 0], [0, -1]]],
    "J": [[[1, 0], [0, 1]], [[0, -1], [-1, 0]]],
    "7": [[[0, -1], [1, 0]], [[-1, 0], [0, 1]]],
    "F": [[[0, -1], [-1, 0]], [[1, 0], [0, 1]]],
    ".": None,
    "S": 0}


def part1(stuff):
    for line in stuff:
        a = line.count("S")
        if a:
            coordinates = [line.index("S"), stuff.index(line)]
    count = 0
    position = [coordinates, 0]
    way = [0, 1]
    while True:
        position[0][0] += way[0]
        position[0][1] += way[1]
        position[1] = stuff[position[0][1]][position[0][0]]
        count += 1
        if position[1] == "S":
            break
        if guide[position[1]] is None:
            break
        elif way in guide[position[1]][0]:
            way = guide[position[1]][1][guide[position[1]][0].index(way)]
        else:
            break
    return count//2


def getpath(stuff):
    for line in stuff:
        a = line.count("S")
        if a:
            coordinates = [line.index("S"), stuff.index(line)]
    path = []
    position = [coordinates, 0]
    way = [0, 1]
    while True:
        position[0][0] += way[0]
        position[0][1] += way[1]
        position[1] = stuff[position[0][1]][position[0][0]]
        print(position)
        path.append(position)
        if position[1] == "S":
            break
        if guide[position[1]] is None:
            break
        elif way in guide[position[1]][0]:
            way = guide[position[1]][1][guide[position[1]][0].index(way)]
        else:
            break
    return path


print(getpath(lines))
