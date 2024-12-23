#!/usr/bin/env python3
import re

from utils import BaseSolution

DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
          'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

def to_digit(affix: str) -> int | None:
   if affix[0].isdigit():
       return int(affix[0])
   for k, v in DIGITS.items():
       if affix.startswith(k):
           return v
   return None

def get_calibration_value(line: str, include_str: bool) -> int:
    if include_str:
        numbers = list(filter(lambda x: x is not None, [to_digit(line[i:]) for i in range(len(line))]))
    else:
        numbers = [int(d) for d in re.findall(r'\d', line)]
    return numbers[0] * 10 + numbers[-1]  # type: ignore

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        return str(sum([get_calibration_value(l, False) for l in ll]))

    def part2(self, ll) -> str:
        return str(sum([get_calibration_value(l, True) for l in ll]))

if __name__ == "__main__":
    Solution()
