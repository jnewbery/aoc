from utils import exit_not_implemented
from itertools import pairwise
import numpy as np
np.set_printoptions(linewidth=10**9)

def part1(ll: list[str]) -> str:
    corners = []
    for l in ll:
        corners.append([int(c) for c in l.split(',')])

    largest = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
            # print(i, corners[i], j, corners[j], area)
            largest = max(area, largest)

    return str(largest)

def part2(ll: list[str]) -> str:
    return exit_not_implemented()
    corners = []
    for l in ll:
        corners.append([int(c) for c in l.split(',')])
    print(corners)

    max_x = max(c[0] for c in corners) + 2
    max_y = max(c[1] for c in corners) + 2

    grid = np.full((max_y, max_x), None, dtype=object)
    # print(grid)

    # draw edges
    for from_corner, to_corner in pairwise(corners + [corners[0]]):
        if from_corner[0] == to_corner[0]:
            x = from_corner[0]
            y_min = min(from_corner[1], to_corner[1])
            y_max = max(from_corner[1], to_corner[1]) + 1
            for y in range(y_min, y_max):
                grid[y][x] = True
        else:
            assert from_corner[1] == to_corner[1]
            y = from_corner[1]
            x_min = min(from_corner[0], to_corner[0])
            x_max = max(from_corner[0], to_corner[0]) + 1
            for x in range(x_min, x_max):
                grid[y][x] = True

    print(grid)

    # flood fill the outside
    to_visit = {(0, 0)}
    while to_visit:
        processing = to_visit.pop()
        grid[processing[1]][processing[0]] = False

        neighbours = [(processing[0] + 1, processing[1]), (processing[0], processing[1] + 1), (processing[0] - 1, processing[1]), (processing[0], processing[1] -1)]
        for n in neighbours:
            if n[0] >= 0 and n[0] < max_x and n[1] >= 0 and n[1] < max_y and (n not in to_visit) and (grid[n[1]][n[0]] == None):
                to_visit.add(n)

    print(grid)

    return ""
