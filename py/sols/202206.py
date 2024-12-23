#!/usr/bin/env python3
from utils import BaseSolution

def find_repeats(l, n):
    for i in range(len(l) - n):
        if len(set(l[i:i + n])) == n:
            return i + n

class Solution(BaseSolution):
    def part1(self, ll):
        return find_repeats(ll[0], 4)

    def part2(self, ll):
        return find_repeats(ll[0], 14)

if __name__ == "__main__":
    Solution()
