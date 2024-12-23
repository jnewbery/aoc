#!/usr/bin/env python3
from utils import BaseSolution

class Solution(BaseSolution):
    def part1(self, ll: list[str]) -> str:
        sol = 0
        for l in ll:
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

        return str(sol)

    def part2(self, ll: list[str]) -> str:
        sol = 0
        while(ll):
            three_lines, ll = ll[:3], ll[3:]
            # print(three_lines)
            # print(set(three_lines[0]))
            # print(set(three_lines[1]))
            # print(set(three_lines[2]))
            badge = (set(three_lines[0]) & set(three_lines[1]) & set(three_lines[2])).pop()
            # print(badge)

            if ord(badge) >= ord('a'):
                pts = (ord(badge) - ord('a') + 1)
            else:
                pts = (ord(badge) - ord('A') + 27)

            # print(pts)
            sol += pts

        return str(sol)

if __name__ == "__main__":
    Solution()
