from utils import exit_not_implemented

def get_joltage(l: list[int]) -> int:
    p1 = 0
    p2 = 1
    for i in range(1, len(l) - 1):
        if l[i] > l[p1]:
            p1 = i
            p2 = i + 1
    for j in range(p1 + 1, len(l)):
        if l[j] > l[p2]:
            p2 = j

    joltage = int(l[p1]) * 10 + int(l[p2])
    return joltage

def part1(ll: list[str]) -> str:
    ret = 0
    for l in ll:
        ret += get_joltage([int(c) for c in l])
    return str(ret)

def part2(ll: list[str]) -> str:
    exit_not_implemented()
    del ll
    return ""
