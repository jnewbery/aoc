import re
from itertools import chain, combinations
from functools import reduce
from operator import xor
import numpy as np
from numpy.typing import NDArray
from utils import exit_not_implemented


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
    return exit_not_implemented()
    pattern = re.compile(
        r'^\[(?P<A>[^\]]+)\]\s+(?P<B>.+?)\s+\{(?P<C>[^}]+)\}$'
    )
    ret = 0
    for l in ll:
        m = pattern.match(l)
        assert m
        _, buttons_str, joltages_str = m.groups()
        # print(buttons_str, joltages_str)

        buttons_list: list[list[int]] = []
        for b_str in re.findall(r"\(([^)]*)\)", buttons_str):
            buttons_list.append([int(l) for l in b_str.split(',')])

        buttons_list.sort(key=lambda b: len(b), reverse=True)
        # print(buttons)

        joltages_list = [int(j) for j in joltages_str.split(',')]
        joltages: NDArray = np.array(joltages_list)
        # joltages = np.array(joltages_list)
        # print(joltages)

        buttons: list[NDArray] = []
        for b in buttons_list:
            b_array = np.zeros_like(joltages)
            for l in b:
                b_array[l - 1] = 1
            buttons.append(b_array)

        # print(buttons)

        # DFS the button presses
        for i in range(len(buttons)):
            if (presses := solve(buttons, i, joltages)) != False:
                ret += presses
                # print(ret)
                break

    return str(ret)
