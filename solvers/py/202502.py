import math

def rep_digit_block_nums_below(x: int) -> set[int]:
    """
    An RDB (repeated-digit-block) number is of the form 'abcabc', eg 183183.
    If the block is n digits, then the RDB number is x * (10^n + 1).

    x * (10^n + 1) is a RDB number for all 10^(n-1) <= x <= 10^n - 1.

    For example, if n is 2, then 1010, 1111, 1212, ..., 9898, 9999 are all RDB numbers.

    This function returns a set of all of the RDB numbers below a given value.
    """
    if x < 10:
        return set()

    digits = int(math.log10(x)) + 1

    rdbns: set[int] = set()
    # find the number of RDB numbers of digit length digits, less than x
    # print(f"{digits=}")
    if digits % 2 == 0:
        n = digits / 2
        top_rdbn = math.floor(x / (10 ** n + 1))
        # print(f"{top_rdbn=}")
        rdbns.update({i * int(10 ** n + 1) for i in range(int(10 ** (n - 1)), top_rdbn + 1)})
        n -= 1
    else:
        n = (digits - 1) / 2

    while n > 0:
        rdbns.update({i * int(10 ** n + 1) for i in range(int(10 ** (n - 1)), int(10 ** n))})
        n -= 1

    return rdbns

def part1(ll: list[str]) -> str:
    invalids: set[int] = set()
    for pair in ll[0].split(','):
        lower, higher = pair.split('-')
        # print(f"{lower=}, {higher=}")
        new_invalids = rep_digit_block_nums_below(int(higher)) - rep_digit_block_nums_below(int(lower) - 1)
        # print(f"{new_invalids=}")
        invalids ^= new_invalids
    return str(sum(invalids))

def part2(ll: list[str]) -> str:
    del ll
    return ""
