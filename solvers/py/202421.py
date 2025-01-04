from functools import cache
import itertools

NUMERIC_KEYPAD: dict[str, tuple[int, int]] = {}
for i in range(1,10):
    x = (i - 1) % 3
    y = (i - 1) // 3 + 1
    NUMERIC_KEYPAD[str(i)] = (x, y)
NUMERIC_KEYPAD["0"] = (1, 0)
NUMERIC_KEYPAD["A"] = (2, 0)

DIRECTIONAL_KEYPAD: dict[str, tuple[int, int]] = { 
    "^": (1, 1),
    "A": (2, 1),
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0)
}

def type_pair(pair: tuple[str, str], numeric: bool) -> set[str]:
    from_point = NUMERIC_KEYPAD[pair[0]] if numeric else DIRECTIONAL_KEYPAD[pair[0]]
    to_point = NUMERIC_KEYPAD[pair[1]] if numeric else DIRECTIONAL_KEYPAD[pair[1]]
    vert_steps = ""
    hor_steps = ""
    if from_point[1] < to_point[1]:
        vert_steps = "^" * (to_point[1] - from_point[1])
    elif from_point[1] > to_point[1]:
        vert_steps = "v" * (from_point[1] - to_point[1])
    if from_point[0] < to_point[0]:
        hor_steps = ">" * (to_point[0] - from_point[0])
    elif from_point[0] > to_point[0]:
        hor_steps = "<" * (from_point[0] - to_point[0])
    if numeric:
        if from_point[0] == 0 and to_point[1] == 0:
            return {hor_steps + vert_steps + "A"}
        elif from_point[1] == 0 and to_point[0] == 0:
            return {vert_steps + hor_steps + "A"}
    else:
        if from_point[0] == 0 and to_point[1] == 1:
            return {hor_steps + vert_steps + "A"}
        elif from_point[1] == 1 and to_point[0] == 0:
            return {vert_steps + hor_steps + "A"}
    return {vert_steps + hor_steps + "A", hor_steps + vert_steps + "A"}

@cache
def solve_string(s: str, depth: int, numeric: bool) -> int:
    # print(f"Processing {s} with depth {depth}")
    if depth == 0:
        return len(s)
    length = 0
    for pair in itertools.pairwise("A" + s):
        # print(pair)
        strings = type_pair(pair, numeric=numeric);
        # print(strings)
        length += min([solve_string(s, depth - 1, False) for s in strings])

    return length

def part1(ll: list[str]) -> str:
    sol = 0
    for l in ll:
        len = solve_string(l, 3, True) 
        numeric_part = int("".join([c for c in l if c.isnumeric()]))
        # print(f"Length: {len} * {numeric_part} = {len * numeric_part}")
        sol += len * numeric_part
    return str(sol)

def part2(ll: list[str]) -> str:
    sol = 0
    for l in ll:
        path_len = solve_string(l, 26, True) 
        numeric_part = int("".join([c for c in l if c.isnumeric()]))
        # print(f"Length: {path_len} * {numeric_part} = {path_len * numeric_part}")
        sol += path_len * numeric_part
    return str(sol)
