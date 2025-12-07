from collections import defaultdict

def part1(ll: list[str]) -> str:
    height, width = len(ll), len(ll[0])
    # The start position is always in the first row
    start = (ll[0].find("S"), 0)

    # path is the cells that are in the path that we haven't yet processed. Since dicts
    # preserve insertion order, we can push new cells onto the 'end' of path, and then pop from the
    # 'front' and ensure that we scan through the frame from top to bottom.
    path: dict[tuple[int, int], bool] = {start: True}
    splitters: int = 0

    while path:
        # pop from the 'front' of the dict
        cell, _ = next(iter(path.items()))
        del path[cell]
        i, j = cell

        if j >= height - 1:
            # reached the bottom
            continue
        elif ll[j + 1][i] == '.':
            # nothing below, path continues down
            path[(i, j + 1)] = True
        elif ll[j + 1][i] == '^':
            # splitter below, path branches. We can only hit the splitter from one
            # cell in the path (directly above), so there's no chance of double counting
            splitters += 1
            if i < width - 1:
                path[(i + 1, j + 1)] = True
            if i > 0:
                path[(i - 1, j + 1)] = True

    return str(splitters)

def part2(ll: list[str]) -> str:
    height, width = len(ll), len(ll[0])
    # The start position is always in the first row
    start = (ll[0].find("S"), 0)

    # quantum_path is the cells that are in the path that we haven't yet processed. Since defaultdicts
    # preserve insertion order, we can push new cells onto the 'end' of quantum_path, and then pop from the
    # 'front' and ensure that we scan through the frame from top to bottom.
    quantum_path: defaultdict[tuple[int, int], int] = defaultdict(int)
    quantum_path[start] = 1
    superpositions = 0

    while quantum_path:
        # pop from the 'front' of the defaultdict
        cell, timelines = next(iter(quantum_path.items()))
        del quantum_path[cell]
        i, j = cell

        if j >= height - 1:
            # reached the bottom. superpositions the quantum superpositions that led us here
            superpositions += timelines
            continue
        elif ll[j + 1][i] == '.':
            # nothing below, path continues down
            quantum_path[(i, j + 1)] += timelines
        elif ll[j + 1][i] == '^':
            # splitter below, path branches. Add superpositions to down-left and down-right.
            if i < width - 1:
                quantum_path[(i + 1, j + 1)] += timelines
            if i > 0:
                quantum_path[(i - 1, j + 1)] += timelines

    return str(superpositions)
