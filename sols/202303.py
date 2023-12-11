#!/usr/bin/env python3
import re

from utils import Solution

class Solution2023(Solution):
    def part1(self, ll):
        leading_digits_match = re.match(r'\d+', input_string)

        numbers:list[dict] =[]
        symbols:list[list] =[]
        for y, l in enumerate(ll):
            numbers.append([])
            symbols.append([])
            for x, c in enumerate(l):
                if c.isdigit():
                    numbers[y].append([x, y, int(c)])
                elif c != '.':
                    symbols[y].append(x)
        return 5

    def part2(self, ll):
        return 10

if __name__ == "__main__":
    Solution2023().run(__file__)
