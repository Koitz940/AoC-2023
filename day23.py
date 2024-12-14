from time import time

with open("readfile") as f:
    lines = f.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].strip()


def part1(stuff):
    y = len(stuff)
    x = len(stuff[0])
    movement = (1, -1, 1j, -1j)
    def path(data, cache, position, steps):
        while True:
            if position.imag == y-1:
                if data[int(position.imag)][int(position.real)] == ".":
                    return steps
                print("last line not .")
                exit(1)
            next_possibles = (position + i for i in movement if y > (position+i).imag > 0 and x > (position+i).real > 0)
            next_possibles = (i for i in next_possibles if i not in cache)
            real_nexts = []
            for i in next_possibles:
                if i not in cache:
                    match data[int(i.imag)][int(i.real)]:
                        case "#":
                            continue
                        case ".":
                            real_nexts.append(i)
                        case "<":
                            if i - position == -1:
                                real_nexts.append(i)
                        case ">":
                            if i - position == 1:
                                real_nexts.append(i)
                        case "^":
                            if i - position == -1j:
                                real_nexts.append(i)
                        case "v":
                            if i - position == 1j:
                                real_nexts.append(i)
            cache.append(position)
            steps += 1
            match len(real_nexts):
                case 0:
                    return 0
                case 1:
                    position = real_nexts[0]
                case _:
                    return max(path(data, cache.copy(), i, steps) for i in real_nexts)
    return path(stuff, [], stuff[0].find(".") + 0j, 0)

def part2(stuff):
    y = len(stuff)
    x = len(stuff[0])
    movement = (1, -1, 1j, -1j)
    cache = []
    intersections = []
    crosses = []
    def findinster(path, position):
        seen = []
        steps = 0
        while True:
            next_possibles = (position + i for i in movement if y > (position + i).imag > 0 and x > (position + i).real > 0)
            next_possibles = (i for i in next_possibles if i not in seen)
            real_nexts = []
            for i in next_possibles:
                match path[int(i.imag)][int(i.real)]:
                    case "#":
                        continue
                    case _:
                        real_nexts.append(i)
            if len(real_nexts) > 1:
                cache.append(previous)
                return steps, position
            steps += 1
            seen.append(position)
            previous = position
            position = real_nexts[0]
    start = findinster(stuff, stuff[0].find(".") + 0j)
    end = findinster(stuff, stuff[-1].find(".") + (y-1)*1j)
    extra = start[0] + end[0]
    crosses.append(start[1])
    crosses.append(end[1])
    def finddistance(path, position):
        next_possibles = (position + i for i in movement if y > (position + i).imag > 0 and x > (position + i).real > 0)
        next_possibles = (i for i in next_possibles if i not in cache)
        real_nexts = []
        for i in next_possibles:
            match path[int(i.imag)][int(i.real)]:
                case "#":
                    continue
                case _:
                    real_nexts.append(i)
        def findinter(begin, coords):
            steps = 0
            while True:
                maybe_next = (coords + i for i in movement if
                                  y > (coords + i).imag > 0 and x > (coords + i).real > 0)
                maybe_next = (i for i in maybe_next if i not in cache and path[int(i.imag)][int(i.real)] != "#")
                followings = []
                if steps == 0:
                    for i in maybe_next:
                        if i not in crosses:
                            followings.append(i)
                else:
                    followings = list(maybe_next)
                match len(followings):
                    case 1:
                        if coords in crosses:
                            intersections.append([begin, coords, steps + 1])
                            findinter(coords, followings[0])
                            return
                        else:
                            steps += 1
                            cache.append(coords)
                            coords = followings[0]
                    case 0:
                        if coords in crosses:
                            intersections.append([begin, coords, steps + 1])
                        return
                    case _:
                        intersections.append([begin, coords, steps + 1])
                        crosses.append(coords)
                        for i in followings:
                            findinter(coords, i)
                        return
        for j in real_nexts:
            findinter(position ,j)
    finddistance(stuff, start[1])
    def findlongest(distances, passed, current, goal):
        if current == goal:
            return 0
        options = (i for i in distances if current in i)
        options = (i for i in options if i[0] not in passed and i[1] not in passed)
        true = []
        for i in options:
            if i[0] == current:
                target = i[1]
            else:
                target = i[0]
            true.append(i[2] + findlongest(distances, passed + [current], target, goal))
        if len(true) == 0:
            return 0
        return max(true)

    return extra + findlongest(intersections, [], start[1], end[1])


