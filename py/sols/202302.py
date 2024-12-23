#!/usr/bin/env python3
from dataclasses import dataclass
import functools

from utils import BaseSolution

@dataclass
class Hand:
    red: int=0
    green: int=0
    blue: int=0

    def contains(self, other: 'Hand') -> bool:
        return self.red >= other.red and self.green >= other.green and self.blue >= other.blue

    @classmethod
    def from_txt(cls, line: str) -> 'Hand':
        red, green, blue = 0, 0, 0
        cubes_strs = line.split(',')
        for color_str in cubes_strs:
            num, color = color_str.split()
            if color == 'red':
                red = int(num)
            elif color == 'green':
                green = int(num)
            elif color == 'blue':
                blue = int(num)
        return cls(red, green, blue)

    def merge(self, other: 'Hand') -> 'Hand':
        return Hand(max(self.red, other.red), max(self.green, other.green), max(self.blue, other.blue))

    def power(self) -> int:
        return self.red * self.green * self.blue

MAX_HAND = Hand(12, 13, 14)

def play_game(line: str) -> bool:
    line = line.split(':')[1].strip()
    for hand in line.split(';'):
        if not MAX_HAND.contains(Hand.from_txt(hand)):
            return False
    return True

def fewest_number(line: str) -> int:
    line = line.split(':')[1].strip()
    return functools.reduce(lambda x, y: x.merge(y), [Hand.from_txt(hand) for hand in line.split(';')]).power()

class Solution(BaseSolution):

    def part1(self, ll: list[str]) -> str:
        ret = 0
        for ix, game in enumerate(ll):
            if play_game(game):
                ret += ix + 1
        return str(ret)

    def part2(self, ll) -> str:
        return str(sum(fewest_number(game) for game in ll))

if __name__ == "__main__":
    Solution()
