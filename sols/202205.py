#!/usr/bin/env python3
from utils import BaseSolution

import re

def make_stacks(ll):
    stacks = [[] for n in range((len(ll[0]) + 1) // 4)]
    # print(stacks)
    while ll and ll[0][:2] != " 1":
        l = ll[0]
        # print(l)
        for i, s in enumerate(stacks):
            c = l[4 * i + 1]
            # print(i, c)
            if c != " ":
                s.append(c)
        ll.pop(0)
    # print(stacks)

    # pop the next two lines
    del ll[:2]
    # print(ll)

    return stacks

class Solution(BaseSolution):
    def part1(self, ll):
        stacks = make_stacks(ll)

        for l in ll:
            repeat, from_stack, to_stack = (int(n) for n in re.findall('[0-9]+', l))
            for r in range(repeat):
                stacks[to_stack - 1].insert(0, stacks[from_stack - 1].pop(0))

        sol = ''.join(a[0] for a in stacks if a)
        return sol

    def part2(self, ll):
        stacks = make_stacks(ll)
        for l in ll:
            repeat, from_stack, to_stack = (int(n) for n in re.findall('[0-9]+', l))
            # stacks list is zero indexed
            from_stack -= 1
            to_stack -= 1
            to_move = stacks[from_stack][:repeat]
            del stacks[from_stack][:repeat]
            stacks[to_stack] = to_move + stacks[to_stack]

        sol = ''.join(a[0] for a in stacks if a)
        return sol

if __name__ == "__main__":
    Solution()
