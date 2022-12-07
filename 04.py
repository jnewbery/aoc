import re

EXAMPLE = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

EXAMPLE_SOL = [2,4]

def part1(lines):
    sol = 0
    for l in lines:
        a_low, a_high, b_low, b_high = (int(a) for a in re.split(",|-", l))
        if a_low <= b_low and a_high >= b_high:
            # print(f"b inside a: {l}")
            sol += 1
        elif a_low >= b_low and a_high <= b_high:
            # print(f"a inside b: {l}")
            sol += 1

    return sol

def part2(lines):
    pass
