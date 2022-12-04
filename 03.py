#!/usr/bin/env python3

EXAMPLE = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def part1(lines):

    sol = 0
    for l in lines:
        line_len = len(l)
        front = set(l[:(line_len >> 1)])
        back = set(l[(line_len >> 1):])
        dup = (front & back).pop()
        # print(dup)

        if ord(dup) >= ord('a'):
            pts = (ord(dup) - ord('a') + 1)
        else:
            pts = (ord(dup) - ord('A') + 27)

        # print(pts)
        sol += pts

    print(f"Part 1: {sol}")

def part2(lines):
    sol = 0
    while(lines):
        ll, lines = lines[:3], lines[3:]
        # print(ll)
        # print(set(ll[0]))
        # print(set(ll[1]))
        # print(set(ll[2]))
        badge = (set(ll[0]) & set(ll[1]) & set(ll[2])).pop()
        # print(badge)

        if ord(badge) >= ord('a'):
            pts = (ord(badge) - ord('a') + 1)
        else:
            pts = (ord(badge) - ord('A') + 27)

        # print(pts)
        sol += pts

    print(f"Part 2: {sol}")
    pass

if __name__ == "__main__":
    f = open('03.txt', 'r')
    if False:
        gen = EXAMPLE.splitlines
    else:
        gen = f.read().splitlines

    part1(gen())
    part2(gen())
