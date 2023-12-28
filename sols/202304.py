#!/usr/bin/env python3
import re

from utils import BaseSolution

def get_winning_numbers_and_numbers_we_have(line: str) -> tuple[set[int], set[int]]:
    line = line.split(":")[1]
    winning_numbers_str, numbers_we_have_str = line.split("|")
    winning_numbers = set(int(x) for x in re.findall(r"\d+", winning_numbers_str))
    numbers_we_have = set(int(x) for x in re.findall(r"\d+", numbers_we_have_str))

    return winning_numbers, numbers_we_have


class Solution(BaseSolution):
    def part1(self, ll):
        score: int = 0
        for l in ll:
            winning_numbers, numbers_we_have = get_winning_numbers_and_numbers_we_have(l)
            overlap = winning_numbers & numbers_we_have
            if overlap:
                score += 2 ** (len(overlap) - 1)
        return score

    def part2(self, ll):
        raise NotImplementedError

if __name__ == "__main__":
    Solution()
