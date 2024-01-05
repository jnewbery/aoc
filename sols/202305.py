#!/usr/bin/env python3
from dataclasses import dataclass
from typing import Iterable
from utils import BaseSolution, get_numbers

@dataclass
class Map:
    ranges: list[tuple[int, int, int]]

    @classmethod
    def from_map_string(cls, map_string: str) -> "Map":
        ranges = []
        for line in map_string:
            nums = get_numbers(line)
            assert len(nums) == 3
            ranges.append((nums[0], nums[1], nums[2]))
        return cls(ranges)

    def apply(self, x: int) -> int:
        for r in self.ranges:
            if r[1] <= x < r[1] + r[2]:
                return x + r[0] - r[1]
        return x

    def __repr__(self) -> str:
        return f"Map({self.ranges})"

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

def apply_maps(maps: list[Map], x: int) -> int:
    for m in maps:
        x = m.apply(x)
    return x

class Solution(BaseSolution):
    def part1(self, ll):
        seeds = get_numbers(ll[0])
        # print(seeds)
        maps = [Map.from_map_string(s) for s in (get_map_strings(ll[2:]))]
        # print(maps)
        return min([apply_maps(maps, s) for s in seeds])

    def part2(self, ll):
        raise NotImplementedError

if __name__ == "__main__":
    Solution()
