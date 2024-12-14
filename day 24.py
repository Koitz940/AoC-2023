import numpy as np
import time

start = time.time()

with open("readfile") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()

fragments = []
for line in range(len(lines)):
    lines[line] = lines[line].replace(" ", "")
    lines[line] = lines[line].split(sep="@")
    lines[line][0] = lines[line][0].split(sep=",")
    lines[line][1] = lines[line][1].split(sep=",")
    position = [int(x) for x in lines[line][0]]
    speed = [int(x) for x in lines[line][1]]
    fragments.append([position, speed])

def part1(stuff, minimum, maximum):
    def valid(solution):
        return 1 if minimum <= solution[0] <= maximum and minimum <= solution[1] <= maximum else 0
    answer = 0
    for i in range(len(stuff)):
        for j in range(i+1, len(stuff)):
            a = np.array([[stuff[i][1][1], -stuff[i][1][0]], [stuff[j][1][1], -stuff[j][1][0]]])
            if np.linalg.det(a) == 0:
                continue
            b = np.array([stuff[i][1][1]*stuff[i][0][0] - stuff[i][0][1]*stuff[i][1][0], stuff[j][1][1]*stuff[j][0][0] - stuff[j][0][1]*stuff[j][1][0]])
            x = np.linalg.solve(a, b)
            if (x[0] - stuff[i][0][0])/stuff[i][1][0] <= 0.001 or (x[0] - stuff[j][0][0])/stuff[j][1][0] <= 0.001:
                continue
            x_tolist = x.tolist()
            answer += valid(x_tolist)
    return answer

print(part1(fragments, 200000000000000, 400000000000000))

end = time.time()

print(end-start)