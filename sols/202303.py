#!/usr/bin/env python3
from utils import BaseSolution
from typing import Optional, Iterable

DIGITS = [str(i) for i in range(10)]

def get_symbols(ll) -> list[set[int]]:
    symbols: list[set[int]] = [set() for _ in range(len(ll))]
    for i, line in enumerate(ll):
        for j, c in enumerate(line):
            if c not in ["."] + DIGITS:
                symbols[i].add(j)
    return symbols

def get_symbols_for_adjacent_rows(symbols: list[set[int]]) -> list[set[int]]:
    symbols_adjacent: list[set[int]] = [set() for _ in range(len(symbols))]
    for i in range(len(symbols)):
        adjacent_rows = [max(i-1, 0), i, min(i+1, len(symbols)-1)]
        symbols_adjacent[i] = set.union(*[symbols[j] for j in adjacent_rows])

    return symbols_adjacent

def get_number_locations(line: str) -> Iterable[tuple[int, set[int]]]:
    """Return a stream of (number, (row, col)) tuples."""
    # Tracks the current number and its starting location
    current_number: Optional[tuple[int, set[int]]] = None

    for i, c in enumerate(line):
        if current_number is None and c in DIGITS:
            current_number = (int(c), {max(i-1, 0), i})
        elif current_number is not None and c in DIGITS:
            current_number = (current_number[0] * 10 + int(c), current_number[1] | {i})
        elif current_number is not None and c not in DIGITS:
            yield (current_number[0], current_number[1] | {i})
            current_number = None

    if current_number is not None:
        yield (current_number[0], current_number[1])


class Solution(BaseSolution):
    def part1(self, ll):
        symbols = get_symbols(ll)
        symbols_adjacent = get_symbols_for_adjacent_rows(symbols)

        sol = 0
        for i, l in enumerate(ll):
            for number, locs in get_number_locations(l):
                if locs & symbols_adjacent[i]:
                    sol += number

        return sol

    def part2(self, ll):
        self.exit_not_implemented()

if __name__ == "__main__":
    Solution()
