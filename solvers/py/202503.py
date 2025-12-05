from utils import exit_not_implemented

def get_best_digit(l: list[int], n: int):
    """
    Get the position of the 'best' digit from a list, excluding the last n digits.

    'best' is the highest digit, with the earliest occurance being the tiebreaker.
    """
    p = 0
    for i in range(1, len(l) - n):
        if l[i] > l[p]:
            p = i
    return p

def get_joltage(l: list[int]) -> int:
    p1 = get_best_digit(l, 1)
    d1 = l[p1]
    l = l[p1 + 1:]

    p2 = get_best_digit(l, 0)
    d2 = l[p2]

    joltage = d1 * 10 + d2
    return(joltage)

def part1(ll: list[str]) -> str:
    ret = 0
    for l in ll:
        ret += get_joltage([int(c) for c in l])
    return str(ret)

def part2(ll: list[str]) -> str:
    exit_not_implemented()
    del ll
    return ""
