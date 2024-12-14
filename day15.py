filename = "readfile"

with open(filename) as f:
    line = f.read()

line = line.strip().split(sep=",")

def algorithm(code):
    answer = 0
    for i in code:
        answer = ((answer + ord(i)) * 17) % 256
    return answer


def part1(stuff):
    return sum(list(map(algorithm, stuff)))


def part2(stuff):
    def hash_turner(code):
        match code.count("="):
            case 1:
                index = code.index("=")
                return [code[:index], algorithm(code[:index]), "=", code[index+1:]]
            case 0:
                index = code.index("-")
                return [code[:index], algorithm(code[:index]), "-"]
    new_list = list(map(hash_turner, stuff))
    boxes_labels = [[] for _ in range(256)]
    boxes = [[] for _ in range(256)]
    for code_info in new_list:
        match code_info[2]:
            case "=":
                if code_info[0] in boxes_labels[code_info[1]]:
                    for j in range(len(boxes[code_info[1]])):
                        if boxes[code_info[1]][j][0] == code_info[0]:
                            boxes[code_info[1]][j] = code_info
                            break
                else:
                    boxes_labels[code_info[1]].append(code_info[0])
                    boxes[code_info[1]].append(code_info)
            case "-":
                if code_info[0] in boxes_labels[code_info[1]]:
                    for j in range(len(boxes[code_info[1]])):
                        if boxes[code_info[1]][j][0] == code_info[0]:
                            boxes[code_info[1]].remove(boxes[code_info[1]][j])
                            boxes_labels[code_info[1]].remove(code_info[0])
                            break
    answer = 0
    for code_info in range(len(boxes)):
        for j in range(len(boxes[code_info])):
            answer += (code_info+1)*(j+1)*int(boxes[code_info][j][3])
    return answer

print(part2(line))