#!/usr/bin/env python3
from utils import BaseSolution

def get_totals(ll):
    totals = [0]
    for l in ll:
        if len(l):
            totals[-1] += int(l)
        else:
            totals.append(0)
    totals.sort()
    return totals

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        totals = get_totals(ll)
        return str(totals[-1])

    def part2(self, ll) -> str:
        totals = get_totals(ll)
        return str(sum(totals[-3:]))

if __name__ == "__main__":
    Solution()
