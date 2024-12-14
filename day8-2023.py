import math
import functools

filename = "readfile"

with open(filename) as f:
    lines = f.readlines()

direction = {
    "R": 2,
    "L": 1
}

modules = []
module_first = []
for line in lines[2:]:
    modules.append([line[0:3], line[7:10], line[12:15]])

for module in modules:
    module_first.append(module[0])
indexes = []
for i in range(len(module_first)):
    if module_first[i][2] == "A":
        indexes.append(i)

currents = []
for i in indexes:
    currents.append(modules[i])


def change_current(current, count, rl):
    target = current[direction[lines[0][rl]]]
    for moduli in modules:
        if moduli[0] == target:
            current = moduli
            break
    count += 1
    rl += 1
    if rl == len(lines[0])-1:
        rl = 0
    return [current, count, rl]


def do(current):
    guide = []
    for node in current:
        count = 0
        rl = 0
        cguide = []
        counts = []
        while True:
            if node[0][2] == "Z":
                check = True
                for n in cguide:
                    if rl == n:
                        check = False
                        break
                if check:
                    cguide.append(rl)
                    counts.append(count)
                else:
                    guide.append(counts[cguide.index(rl)])
                    break
            following = change_current(node, count, rl)
            node = following[0]
            count = following[1]
            rl = following[2]
    return functools.reduce(math.lcm, guide)


print(do(currents))
