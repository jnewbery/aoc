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
    while i < len(pairs):
        pair = pairs[i]
        if len(str(pair[0])) != len(str(pair[1])):
            pairs.pop(i)
            pairs.insert(i, (10 ** len(str(pair[0])), pair[1]))
            pairs.insert(i, (pair[0], 10 ** len(str(pair[0])) - 1))
        else:
            i += 1

    return pairs

def sum_rep_digit_block_nums_between(lower: int, higher: int) -> int:
    rdbns: set[int] = set()
    for repeats in range(2, len(str(lower)) + 1):
        rdbns |= sum_rep_n_digit_block_nums_between(lower, higher, repeats)

    return sum(rdbns)


def sum_rep_n_digit_block_nums_between(lower: int, higher: int, repeats: int) -> set[int]:
    """
    An R2DB (repeated-n-digit-block) number is of the form 'abcabc' (repeated repeats times), eg 183183.
    If the block is block_len digits, then the RDB number is x * (10^m + 1).

    x * (10^m + 1) is a R2DB number for all 10^(repeats-1) <= x <= 10^m - 1.

    For example, if m is 2, then 1010, 1111, 1212, ..., 9898, 9999 are all R2DB numbers.

    This function returns the set of all of the RnDB numbers below a given value, with a length equal to the given value.
    """
    digits = int(math.log10(lower)) + 1

    if digits % repeats != 0:
        return set()

    # Find the RDB numbers of digit length digits, less than higher but more than lower
    block_len = digits / repeats
    divisor = int(int(str(int(10 ** (block_len - 1))) * repeats) / int(10 ** (block_len - 1)))
    bottom_rdbn = math.ceil(lower / divisor)
    top_rdbn = math.floor(higher / divisor)
    rdbs = {i * divisor for i in range(bottom_rdbn, top_rdbn + 1)}
    return rdbs

def part1(ll: list[str]) -> str:
    invalids: int = 0
    pairs: list[tuple[int, int]] = []
    for str_pair in ll[0].split(','):
        pair = str_pair.split('-')
        pairs.append((int(pair[0]), int(pair[1])))
    pairs = merge_and_split(pairs)

    for pair in pairs:
        invalids += sum(sum_rep_n_digit_block_nums_between(*pair, 2))
    return str(invalids)

def part2(ll: list[str]) -> str:
    invalids: int = 0
    pairs: list[tuple[int, int]] = []
    for str_pair in ll[0].split(','):
        pair = str_pair.split('-')
        pairs.append((int(pair[0]), int(pair[1])))
    pairs = merge_and_split(pairs)

    for pair in pairs:
        invalids += sum_rep_digit_block_nums_between(*pair)
    return str(invalids)
