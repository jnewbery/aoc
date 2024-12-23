#!/usr/bin/env python3
from utils import BaseSolution

import functools

def get_pairs(ll):
    while ll:
        a = eval(ll.pop(0))
        b = eval(ll.pop(0))
        if ll:
            ll.pop(0)  # empty line
        yield a, b

def compare(a, b):
    # print(f"comparing {a} and {b}")
    if type(a) == int and type(b) == int:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    elif type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            comp = compare(a[i], b[i])
            if comp != 0:
                return comp
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0
    elif type(a) == list and type(b) == int:
        return compare(a, [b])
    elif type(b) == list and type(a) == int:
        return compare([a], b)

class Solution(BaseSolution):
    def part1(self, ll):
        sol = 0
        for i, pair in enumerate(get_pairs(ll)):
            # print(i + 1, pair)
            if compare(pair[0], pair[1]) == -1:
                # print("in order")
                sol += i + 1
        return sol

    def part2(self, ll):
        signals = [eval(l) for l in ll if l]
        signals += [[[2]], [[6]]]
        signals.sort(key=functools.cmp_to_key(compare))
        return (signals.index([[2]]) + 1) * (signals.index([[6]]) + 1)

if __name__ == "__main__":
    Solution()
