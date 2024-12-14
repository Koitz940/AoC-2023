with open("readfile") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()
    lines[line] = lines[line].split()

def part1(stuff):
    directions = {
        "R": 1,
        "L": -1,
        "U": -1j,
        "D": 1j}
    path = set()
    position = complex(0,0)
    path.add(position)
    for i in stuff:
        for j in range(int(i[1])):
            position += directions[i[0]]
            path.add(position)
    xmax = int(max(i.real for i in path) + 1)
    ymin = int(min(i.imag for i in path))
    ymax = int(max(i.imag for i in path) + 1)
    xmin = int(min(i.real for i in path))

    def inside(point):
        start = point
        if point in path:
            return 1
        for way in (1, -1, 1j, -1j):
            point = start
            while point not in path:
                point += way
                if not (xmin < point.real < xmax-1 and ymin < point.imag < ymax-1):
                    return 0
        return 1
    print(len(path))
    count = 0
    for t in range(xmin, xmax):
        for s in range(ymin, ymax):
            coord = t + 1j*s
            count += inside(coord)
    return count


print(part1(lines))