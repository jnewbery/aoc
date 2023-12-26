#!/usr/bin/env python3
from utils import BaseSolution

class Solution(BaseSolution):
    def part1(self, lines):
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

        return sol

    def part2(self, lines):
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

        return sol

if __name__ == "__main__":
    Solution()
