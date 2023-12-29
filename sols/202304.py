#!/usr/bin/env python3
import re

from utils import BaseSolution

def get_winning_numbers_and_numbers_we_have(line: str) -> tuple[set[int], set[int]]:
    line = line.split(":")[1]
    winning_numbers_str, numbers_we_have_str = line.split("|")
    winning_numbers = set(int(x) for x in re.findall(r"\d+", winning_numbers_str))
    numbers_we_have = set(int(x) for x in re.findall(r"\d+", numbers_we_have_str))

    return winning_numbers, numbers_we_have

def get_number_overlaps(l: str) -> int:
    winning_numbers, numbers_we_have = get_winning_numbers_and_numbers_we_have(l)
    return len(winning_numbers & numbers_we_have)

def overlaps_to_score(overlaps: int) -> int:
    if overlaps == 0:
        return 0
    return 2 ** (overlaps - 1)

class Solution(BaseSolution):
    def part1(self, ll):
        return sum(overlaps_to_score(get_number_overlaps(l)) for l in ll)

    def part2(self, ll):
        cards = [1 for l in ll]
        for i in range(len(ll)):
            overlaps = get_number_overlaps(ll[i])
            for j in range(overlaps):
                cards[i + j + 1] += cards[i]
        return sum(cards)

if __name__ == "__main__":
    Solution()
