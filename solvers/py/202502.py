import math

def merge_and_split(pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Given a list of ranges:
    - merge any overlapping or adjacent ranges so that no range overlaps
    - split ranges by number of digits, eg [[97, 105]] becomes [[97, 99], [100, 105]]
    """
    pairs.sort()

    i = 0
    while i < len(pairs) - 1:
        if pairs[i][1] >= pairs[i + 1][0] - 1:
            # merge ranges
            pairs[i] = (pairs[i][0], max(pairs[i][1], pairs[i + 1][1]))
            pairs.pop(i + 1)
        else:
            i += 1

    i = 0
    while i < len(pairs) - 1:
        pair = pairs[i]
        if len(str(pair[0])) != len(str(pair[1])):
            pairs.pop(i)
            pairs.insert(i, (10 ** len(str(pair[0])), pair[1]))
            pairs.insert(i, (pair[0], 10 ** len(str(pair[0])) - 1))
            i += 2
        else:
            i += 1

    return pairs


def sum_rep_2_digit_block_nums_between(lower: int, higher: int) -> int:
    """
    An R2DB (repeated-2-digit-block) number is of the form 'abcabc', eg 183183.
    If the block is n digits, then the RDB number is x * (10^n + 1).

    x * (10^n + 1) is a RDB number for all 10^(n-1) <= x <= 10^n - 1.

    For example, if n is 2, then 1010, 1111, 1212, ..., 9898, 9999 are all RDB numbers.

    This function returns a sum of all of the RDB numbers below a given value, with a length equal to the given value.
    """
    # assert len(str(lower)) == len(str(higher)), "Solver only implemented for pairs of numbers of length differing by at most one"
    digits = int(math.log10(lower)) + 1

    if digits % 2 != 0:
        return 0

    # Find the RDB numbers of digit length digits, less than higher but more than lower
    n = digits / 2
    top_rdbn = math.floor(higher / (10 ** n + 1))
    bottom_rdbn = math.ceil(lower / (10 ** n + 1))
    rdbs = [i * int(10 ** n + 1) for i in range(bottom_rdbn, top_rdbn + 1)]
    # print(f"{rdbs=}")
    # print(f"{sum(rdbs)=}")
    return sum(rdbs)

def part1(ll: list[str]) -> str:
    invalids: int = 0
    pairs: list[tuple[int, int]] = []
    for str_pair in ll[0].split(','):
        pair = str_pair.split('-')
        pairs.append((int(pair[0]), int(pair[1])))
    pairs = merge_and_split(pairs)

    for pair in pairs:
        new_invalids = sum_rep_2_digit_block_nums_between(*pair)
        invalids += new_invalids
    return str(invalids)

def part2(ll: list[str]) -> str:
    for pair in ll[0].split(','):
        lower, higher = pair.split('-')
        assert abs(len(lower) - len(higher)) <= 1, "Solver only implemented for pairs of numbers of length differing by at most one"
    return ""
