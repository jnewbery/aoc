import re
from itertools import chain, combinations
from functools import reduce
from operator import xor
import numpy as np
from numpy.typing import NDArray
from scipy.optimize import milp, LinearConstraint, Bounds


def part1(ll: list[str]) -> str:
    ret = 0
    pattern = re.compile(
        r'^\[(?P<A>[^\]]+)\]\s+(?P<B>.+?)\s+\{(?P<C>[^}]+)\}$'
    )
    for l in ll:
        m = pattern.match(l)
        assert m
        target_str, buttons_str, _ = m.groups()
        target = int(target_str.replace('.', '0').replace('#', '1')[::-1], 2)

        buttons: list[int] = []
        for b_str in re.findall(r"\(([^)]*)\)", buttons_str):
            b = sum([2 ** int(n) for n in b_str.split(',')])
            buttons.append(b)

        # BFS the different button combinations
        for subset in chain.from_iterable(combinations(buttons, n) for n in range(len(buttons))):
            lights = reduce(xor, subset, 0)
            if lights == target:
                ret += len(subset)
                # print(subset, lights)
                # print("success")
                break


    return str(ret)

def solve(buttons: list[NDArray], button_ix: int, target: NDArray) -> int | bool:
    # print(buttons[button_ix], target)
    target -= buttons[button_ix]
    if (target < 0).any():
        target += buttons[button_ix]
        return False
    if (target == 0).all():
        return 1

    for i in range(button_ix, len(buttons)):
        ret = solve(buttons, i, target)
        if ret != False:
            return ret + 1

    target += buttons[button_ix]
    return False


def part2(ll: list[str]) -> str:
    pattern = re.compile(
        r'^\[(?P<A>[^\]]+)\]\s+(?P<B>.+?)\s+\{(?P<C>[^}]+)\}$'
    )
    ret = 0
    for l in ll:
        m = pattern.match(l)
        assert m
        _, buttons_str, joltages_str = m.groups()
        # print(buttons_str, joltages_str)

        joltages_list = [int(j) for j in joltages_str.split(',')]
        joltages: NDArray = np.array(joltages_list, dtype=float)

        buttons_strings: list[str] = re.findall(r"\(([^)]*)\)", buttons_str)
        buttons: NDArray = np.zeros((len(buttons_strings), len(joltages)), dtype=int)
        for i, b_str in enumerate(buttons_strings):
            counters = [int(l) for l in b_str.split(',')]
            buttons[i][counters] = 1
        buttons = buttons.transpose()

        num_buttons = len(buttons_strings)
        c = np.ones(num_buttons, dtype=float)

        # Equality constraint: A_eq x = b_eq
        eq_con = LinearConstraint(buttons, lb=joltages, ub=joltages)  # pyright: ignore

        # Non-negative variables: x_i >= 0 (no upper bound)
        bounds = Bounds(lb=np.zeros(num_buttons), ub=np.full(num_buttons, np.inf))  # pyright: ignore

        # All variables must be integer
        integrality = np.ones(num_buttons, dtype=int)

        res = milp(
            c=c,
            constraints=[eq_con],
            bounds=bounds,
            integrality=integrality,
        )

        ret += int(round(res.fun))

    return str(ret)
