#!/usr/bin/env python3
from utils import BaseSolution

import itertools

def construct_grid(ll):
    # Construct grid of (x,y,z) coordinates
    grid = []
    for y, l in enumerate(ll):
        grid.append([])
        for x, c in enumerate(l):
            grid[-1] += [(x, y, int(c))]

    # for l in grid:
    #     print(l)

    return grid

def visible(row):
    # Return set of all trees visible along a line of sight
    vis = set()
    tallest = -1
    for tree in row:
        if tree[2] > tallest:
            tallest = tree[2]
            vis.add(tree)

    # print(vis)
    return vis

def visible_from(row):
    # Return number of trees visible along a line from a height
    # print(row)
    height = row.pop(0)[2]
    ret = 0
    for tree in row:
        ret += 1
        if tree[2] >= height:
            break

    # print(ret)
    return ret

class Solution(BaseSolution):
    def part1(self, ll: list[str]) -> str:
        grid = construct_grid(ll)
        vis = set()

        for row in grid:
            vis |= visible(row)
            vis |= visible(reversed(row))
        transposed_grid = list(zip(*grid))
        for row in transposed_grid:
            vis |= visible(row)
            vis |= visible(reversed(row))

        return str(len(vis))

    def part2(self, ll) -> str:
        grid = construct_grid(ll)

        sol = 0
        for x, y in itertools.product(range(1, len(grid[0]) - 1), range(1, len(grid) - 1)):
            # print(f"({x},{y})")
            scenic = visible_from(grid[y][x:])
            scenic *= visible_from(list(reversed(grid[y][:x + 1])))
            scenic *= visible_from([grid[i][x] for i in range(y, len(grid))])
            scenic *= visible_from(list(reversed([grid[i][x] for i in range(y + 1)])))

            # print(f"({x},{y}): {scenic}")
            if scenic > sol:
                sol = max(sol, scenic)

        return str(sol)

if __name__ == "__main__":
    Solution()
