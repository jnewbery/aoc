from itertools import product
from collections import defaultdict

def part1(ll: list[str]) -> str:
    height, width = len(ll), len(ll[0])
    start = (ll[0].find("S"), 0)

    splitters: int = 0
    to_visit: dict[tuple[int, int], bool] = {start: True}

    while to_visit:
        key, _ = next(iter(to_visit.items()))
        i, j = key
        del to_visit[key]
        if j >= height - 1:
            # reached the bottom
            continue
        elif ll[j + 1][i] == '.':
            to_visit[(i, j + 1)] = True
        elif ll[j + 1][i] == '^':
            splitters += 1
            if (i + 1) <= width:
                to_visit[(i + 1, j + 1)] = True
            if (i - 1) >= 0:
                to_visit[(i - 1, j + 1)] = True

    return str(splitters)

def part2(ll: list[str]) -> str:
    height, width = len(ll), len(ll[0])
    quantum_path: defaultdict[tuple[int, int], int] = defaultdict(int)
    count = 0

    for i, j in product(range(width), range(height)):
        if ll[j][i] == "S":
            quantum_path[(i, j)] = 1
            break

    while quantum_path:
        pos, timelines = next(iter(quantum_path.items()))
        del quantum_path[pos]
        i, j = pos
        if j >= height - 1:
            # reached the bottom
            count += timelines
            continue
        elif ll[j + 1][i] == '.':
            quantum_path[(i, j + 1)] += timelines
        elif ll[j + 1][i] == '^':
            if (i + 1) <= width:
                quantum_path[(i + 1, j + 1)] += timelines
            if (i - 1) >= 0:
                quantum_path[(i - 1, j + 1)] += timelines

    return str(count)
