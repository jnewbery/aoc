import itertools

def adjacents(coord, grid):
    if (coord[0] - 1, coord[1]) in grid:
        yield (coord[0] - 1, coord[1])
    if (coord[0], coord[1] - 1) in grid:
        yield (coord[0], coord[1] - 1)
    if (coord[0] + 1, coord[1]) in grid:
        yield (coord[0] + 1, coord[1])
    if (coord[0], coord[1] + 1) in grid:
        yield (coord[0], coord[1] + 1)

def solve(ll, part):
    heights = {}
    distances = [[]]

    goal = None
    for y, l in enumerate(ll):
        for x, c in enumerate(l):
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                if part == 1 or ord(c) >= ord('b'):
                    heights[(x, y)] = ord(c) - ord('a')
                elif part == 2 and ord(c) == ord('a'):
                    distances[0] += [(x, y, 0)]
            elif c == 'S':
                distances[0] += [(x, y, 0)]
            elif c == 'E':
                heights[(x, y)] = ord('z') - ord('a')
                goal = (x, y)
    assert goal is not None

    # print(heights)
    # print(distances)
    for d in itertools.count():
        distances.append([])
        for coord in distances[d]:
            for adjacent in adjacents(coord, heights):
                # print(adjacent)
                if heights[adjacent] <= coord[2] + 1:
                    if adjacent[0] == goal[0] and adjacent[1] == goal[1]:
                        return len(distances) - 1

                    distances[-1].append((adjacent[0], adjacent[1], heights[adjacent]))
                    del heights[adjacent]

            # print(distances)

def part1(ll: list[str]) -> str:
    return str(solve(ll, 1))

def part2(ll: list[str]) -> str:
    return str(solve(ll, 2))
