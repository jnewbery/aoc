import re

def get_numbers(l):
    return (int(a) for a in re.split(",|-", l))

def part1(ll: list[str]) -> str:
    sol = 0
    for l in ll:
        a_low, a_high, b_low, b_high = get_numbers(l)
        if a_low <= b_low and a_high >= b_high:
            # print(f"b inside a: {l}")
            sol += 1
        elif a_low >= b_low and a_high <= b_high:
            # print(f"a inside b: {l}")
            sol += 1

    return str(sol)

def part2(ll: list[str]) -> str:
    sol = 0
    for l in ll:
        a_low, a_high, b_low, b_high = get_numbers(l)
        if not (a_high < b_low or b_high < a_low):
            # print(f"overlap: {l}")
            sol += 1

    return str(sol)
