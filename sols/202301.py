#!/usr/bin/env python3
import argparse
from typing import Optional

from utils import get_params, exit_not_implemented

DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
          'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

def to_digit(affix: str) -> Optional[int]:
   if affix[0].isdigit():
       return int(affix[0])
   for k, v in DIGITS.items():
       if affix.startswith(k):
           return v
   return None

def get_calibration_value(line: str) -> int:
    numbers = list(filter(lambda x: x is not None, [to_digit(line[i:]) for i in range(len(line))]))
    return numbers[0] * 10 + numbers[-1]

def part1(ll):
    exit_not_implemented()

def part2(ll):
    return sum([get_calibration_value(l) for l in ll])

if __name__ == "__main__":
    part, problem_input = get_params(__file__)

    if part == "1":
        print(part1(problem_input.splitlines()))
    elif part == "2":
        print(part2(problem_input.splitlines()))
