filename = "calibration_document"

with open(filename) as f:
    lines = f.readlines()

    seeds = lines[0].split()
    seeds = seeds[1:]
    seeds = list(map(int, seeds))


def create_seeds_part2(seed):
    pairs = []
    for i in range(0, len(seed)-1, 2):
        pair = [seed[i], seed[i+1]]
        pairs.append(pair)
    return pairs


paths = []
sections = []

for line in range(len(lines)):
    if lines[line] == "\n":
        sections.append(line)

for section in range(len(sections)-1):
    path = []
    for line in range(sections[section] + 1, sections[section+1]-1):
        wanted = lines[line+1].split()
        wanted = list(map(int, wanted))
        path.append(wanted)
    paths.append(path)


def part1(plantegg):
    for way in paths:
        for matching in way:
            if matching[1] <= plantegg < matching[1] + matching[2]:
                plantegg += matching[0] - matching[1]
                break
    return plantegg


def part2(pair, turn):
    if turn + 1 != len(paths):     # not time to return a number because not location time
        for matching in paths[turn]:
            if matching[1] <= pair[0] < matching[1] + matching[2]:
                if pair[0] + pair[1] <= matching[1] + matching[2]:    # whole range of seed in 1 match
                    return part2([matching[0] + pair[0] - matching[1], pair[1]], turn + 1)
                else:    # range of seed in different matches
                    passing_pair = [matching[0] + pair[0] - matching[1], matching[2] + matching[1] - pair[0]]
                    staying_pair = [matching[1] + matching[2], pair[1] - (matching[2] + matching[1] - pair[0])]
                    return min(part2(passing_pair, turn + 1), part2(staying_pair, turn))
        return part2(pair, turn + 1)   # seed not in a range
    else:      # time for location, so time to return a number
        for matching in paths[turn]:
            if matching[1] <= pair[0] < matching[1] + matching[2]:
                if pair[0] + pair[1] <= matching[1] + matching[2]:  # whole range of seed in 1 match
                    return matching[0] + pair[0] - matching[1]   # returning the smaller number
                else:   # range of seed in different matches
                    still_running_pair = [matching[2] + matching[1], pair[1]-(matching[2] + matching[1] - pair[0])]
                    return min(matching[0] + pair[0] - matching[1], part2(still_running_pair, turn))
        return pair[0]     # seed not in a range


print(min(map(part2, create_seeds_part2(seeds), [0 for x in range(len(create_seeds_part2(seeds)))])))
