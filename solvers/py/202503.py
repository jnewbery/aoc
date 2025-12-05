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

def get_n_joltage(l: list[int], n: int) -> int:
    """
    Get the joltage of length n
    """
    joltage = 0
    for i in range(n):
        joltage *= 10
        p = get_best_digit(l, n - i - 1)
        joltage += l[p]
        l = l[p + 1:]

    return(joltage)

def part1(ll: list[str]) -> str:
    ret = 0
    for l in ll:
        ret += get_n_joltage([int(c) for c in l], 2)
    return str(ret)

def part2(ll: list[str]) -> str:
    ret = 0
    for l in ll:
        ret += get_n_joltage([int(c) for c in l], 12)
    return str(ret)
