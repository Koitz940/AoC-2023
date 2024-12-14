filename = "calibration_document"

with open(filename) as f:
    lines = f.readlines()


def beat(time_available, distance):
    for time in range(1, time_available + 1):
        if time * (time_available - time) > distance:
            return time_available - 2 * time + 1


def part1(self):
    answer = 1
    times = self[0].split()
    distances = self[1].split()
    for j in range(1, len(times)):
        answer *= beat(int(times[j]), int(distances[j]))
    return answer


def part2(self):
    time = ""
    distance = ""
    times = self[0].split()
    distances = self[1].split()
    for i in range(1, len(times)):
        time += times[i]
        distance += distances[i]
    return beat(int(time), int(distance))
