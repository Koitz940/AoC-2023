filename = "readfile"

with open(filename) as f:
    lines = f.readlines()


def solve(stuff, distance):
    rows = []
    for line in range(len(stuff)):
        if "#" not in stuff[line]:
            rows.append(line)
    columns = []
    for i in range(len(stuff[0])):
        if "#" not in [stuff[j][i] for j in range(len(stuff))]:
            columns.append(i)
    galaxies = []
    for i in range(len(stuff)):
        for j in range(len(lines[i])):
            if stuff[i][j] == "#":
                galaxies.append([i, j])
    for galaxy in galaxies:
        rows_used = [i for i in rows if i < galaxy[0]]
        galaxy[0] += distance * len(rows_used)
        columns_used = [i for i in columns if i < galaxy[1]]
        galaxy[1] += distance * len(columns_used)
    answer = 0
    for i in range(len(galaxies)):
        for j in range(i):
            answer += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return answer
