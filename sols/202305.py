#!/usr/bin/env python3
from typing import Iterable
from utils import BaseSolution, get_numbers

class

def get_map_strings(ll: list[str]) -> Iterable[list[str]]:
    ret: list[str] = []
    for l in ll:
        if "map" in l:
            ret = []
        elif len(l) == 0:
            yield ret
        else:
            ret.append(l)
    yield ret


class Solution(BaseSolution):
    def part1(self, ll):
        seeds = get_numbers(ll[0])
        print(seeds)
        map_strings = list(get_map_strings(ll[2:]))
        print(map_strings)

    def part2(self, ll):
        raise NotImplementedError

if __name__ == "__main__":
    Solution()
