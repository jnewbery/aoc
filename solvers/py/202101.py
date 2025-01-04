from itertools import pairwise

def part1(ll: list[str]) -> str:
    depths = [int(l) for l in ll]
    return str(sum(b > a for a, b in pairwise(depths)))

def part2(ll: list[str]) -> str:
    depths = [int(l) for l in ll]
    windows = [sum(depths[i:i+3]) for i in range(len(depths) - 2)]
    return str(sum(b > a for a, b in pairwise(windows)))
