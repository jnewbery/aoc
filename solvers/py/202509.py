from utils import exit_not_implemented

def part1(ll: list[str]) -> str:
    corners = []
    for l in ll:
        corners.append([int(c) for c in l.split(',')])

    # print(corners)

    largest = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
            # print(i, corners[i], j, corners[j], area)
            largest = max(area, largest)

    return str(largest)

def part2(ll: list[str]) -> str:
    exit_not_implemented()
    del ll
    return ""
