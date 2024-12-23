#!/usr/bin/env python3
from utils import BaseSolution
from typing import Generator

from itertools import count

def get_pairs(ll) -> Generator[tuple[tuple[int, int], tuple[int, int]], None, None]:
    for l in ll:
        coords = l.split(" -> ")
        int_coords: list[tuple[int, int]] = []
        for coord in coords:
            x, y = coord.split(",")
            int_coords.append((int(x), int(y)))

        for i in range(len(int_coords) - 1):
            yield (int_coords[i], int_coords[i + 1])

def get_rocks(p: tuple[tuple[int, int], tuple[int, int]]) -> list[list[int]]:
    if p[0][0] != p[1][0]:
        return [[x, p[0][1]] for x in range(min(p[0][0], p[1][0]), max(p[0][0], p[1][0]) + 1)]
    elif p[0][1] != p[1][1]:
        return [[p[0][0], y] for y in range(min(p[0][1], p[1][1]), max(p[0][1], p[1][1]) + 1)]
    assert False, "invalid pairs"

def print_cave(cave):
    print('-' * len(cave[0]))
    for y in cave:
        print(''.join(y))

def add_sand(cave: list[list[str]], start: list[int]) -> tuple[int, int]:
    sand = start.copy()
    while True:
        if cave[sand[0] + 1][sand[1]] == '.':
            sand[0] += 1
        elif cave[sand[0] + 1][sand[1] - 1] == '.':
            sand[0] += 1
            sand[1] -= 1
        elif cave[sand[0] + 1][sand[1] + 1] == '.':
            sand[0] += 1
            sand[1] += 1
        else:
            cave[sand[0]][sand[1]] = 'o'
            return sand[0], sand[1]

def get_cave(ll):
    rocks = []
    for p in get_pairs(ll):
        rocks += get_rocks(p)
        # print(p)
    # print(rocks)

    max_y = max(r[1] for r in rocks) + 3
    min_x = 500 - max_y
    # print(max_y)

    # shift x axis by min_x
    for rock in rocks:
        rock[0] -= (min_x)
    # print(rocks)

    entrance = [0, 500 - min_x]

    cave = [['.' for _ in range(2 * max_y)] for _ in range(max_y)]
    # print_cave(cave)

    for rock in rocks:
        cave[rock[1]][rock[0]] = '#'
    for x in range(len(cave[0])):
        cave[-1][x] = '#'
    cave[entrance[0]][entrance[1]] = '+'
    # print_cave(cave)

    return (cave, entrance)

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        cave, entrance = get_cave(ll)
        for n in count():
            new_sand = add_sand(cave, entrance)
            if new_sand[0] == len(cave) - 2:
                return str(n)
            # time.sleep(0.01)
            # print("\033c", end="\033[A")
            # print_cave(cave)
        assert False, "No solution found"

    def part2(self, ll) -> str:
        cave, entrance = get_cave(ll)
        # print_cave(cave)
        for n in count():
            new_sand = add_sand(cave, entrance)
            if new_sand[0] == entrance[0] and new_sand[1] == entrance[1]:
                return str(n + 1)
        assert False, "No solution found"

if __name__ == "__main__":
    Solution()
