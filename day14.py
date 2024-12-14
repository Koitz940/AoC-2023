with open("readfile") as f:
    lines = f.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip()

for line in range(len(lines)):
    lines[line] = [z for z in lines[line]]


def transpose(thing):
    rows = len(thing)
    cols = len(thing[0])
    return [[thing[i][j] for i in range(rows)] for j in range(cols)]


def part1(stuff):
    for i in range(len(stuff)-1, -1, -1):
        for j in range(i):
            for element in range(len(stuff[j+1])):
                if stuff[j+1][element] == "O" and stuff[j][element] == ".":
                    stuff[j + 1][element], stuff[j][element] = stuff[j][element], stuff[j + 1][element]
    answer = 0
    for i in range(len(stuff)):
        answer += (len(stuff)-i)*stuff[i].count("O")
    return answer


def part2(stuff):
    def tilt(state, direction):
        match direction:
            case 1:
                for ind in range(len(state) - 1, -1, -1):
                    for j in range(ind):
                        for element in range(len(state[0])):
                            if state[j + 1][element] == "O" and state[j][element] == ".":
                                state[j + 1][element], state[j][element] = state[j][element], state[j + 1][element]
            case -1:
                for ind in range(len(state), 0, -1):
                    for j in range(len(state)-ind, 0, -1):
                        for element in range(len(state[0])):
                            if state[j - 1][element] == "O" and state[j][element] == ".":
                                state[j - 1][element], state[j][element] = state[j][element], state[j - 1][element]
        return state


    def do_cycle(state):
        state = tilt(state,1)
        state = tilt(transpose(state), 1)
        state = tilt(transpose(state), -1)
        state = tilt(transpose(state), -1)
        return transpose(state)


    def answ(state):
        answer = 0
        for i in range(len(state)):
            answer += (len(state) - i) * state[i].count("O")
        return answer


    count = 0
    grid = stuff
    passed_states = [stuff.copy()]
    while count < 1000000000:
        grid = do_cycle([[i for i in j.copy()] for j in grid])
        if grid in passed_states:
            check = (1000000000 - passed_states.index(grid)) % (count + 1 - passed_states.index(grid)) + passed_states.index(grid)
            for i in passed_states[check]:
                print(i)
            return answ(passed_states[check])
        count += 1
        passed_states.append(grid)

