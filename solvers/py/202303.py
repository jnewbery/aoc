import math, re

DIGITS = [str(i) for i in range(10)]

def get_symbols(ll) -> dict[tuple[int, int], list[int]]:
    """Returns dict of (x,y) -> [] for all symbols in the grid."""
    board_width = len(ll[0])
    board_height = len(ll)
    symbols: dict[tuple[int,int], list[int]] = {(r, c): [] for r in range(board_width) for c in range(board_height)
                    if ll[r][c] not in '01234566789.'}

    for r, row in enumerate(ll):
        # Find every cell boardering a number
        for n in re.finditer(r'\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1)
                           for c in range(n.start()-1, n.end()+1)}

            # For every cell boardering a number, assign that number as a score to the cell
            # Assumes that no number touches more than one symbol (otherwise it'd be counted twice for part 1)
            for o in edge & symbols.keys():
                symbols[o].append(int(n.group()))

    return symbols

def part1(ll: list[str]) -> str:
    symbols = get_symbols(ll)

    return str(sum(sum(p) for p in symbols.values()))

def part2(ll: list[str]) -> str:
    symbols = get_symbols(ll)

    # Assumes that no other symbol (eg & or #) touches two numbers
    return str(sum(math.prod(p) for p in symbols.values() if len(p)==2))
