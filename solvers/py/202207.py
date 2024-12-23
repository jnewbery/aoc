#!/usr/bin/env python3
from utils import BaseSolution

from collections import defaultdict
from itertools import accumulate

def get_directories(ll):
    counted_files = set()
    dirs = defaultdict(int)

    curr = []
    for l in ll:
        match l.split():
            case '$', 'cd', '/': curr = ['/']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, filename:
                full_filename = "".join(curr) + filename
                if full_filename not in counted_files:
                    counted_files.add(full_filename)
                    for p in accumulate(curr):
                        dirs[p] += int(size)

    return dirs

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        directories = get_directories(ll)

        sol = 0
        for v in directories.values():
            if v <= 100000:
                sol += v

        return str(sol)

    def part2(self, ll) -> str:
        directories = get_directories(ll)
        target = directories[("/")] - 40000000
        sol = min(x for x in directories.values() if x > target)
        return str(sol)

if __name__ == "__main__":
    Solution()
