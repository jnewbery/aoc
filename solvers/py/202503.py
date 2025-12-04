from utils import exit_not_implemented

def get_joltage(l: str) -> int:
    p1 = 0
    p2 = 1
    for i in range(1, len(l) - 1):
        if int(l[i]) > int(l[p1]):
            p1 = i
            p2 = i + 1
    for j in range(p1 + 1, len(l)):
        # print(p1, p2, j)
        if int(l[j]) > int(l[p2]):
            p2 = j
    # print(p1, p2)
    joltage = int(l[p1]) * 10 + int(l[p2])
    # print(joltage)
    return joltage

def part1(ll: list[str]) -> str:
    ret = 0
    for l in ll:
        ret += get_joltage(l)
    return str(ret)

def part2(ll: list[str]) -> str:
    exit_not_implemented()
    del ll
    return ""
