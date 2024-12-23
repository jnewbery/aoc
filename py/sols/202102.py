#!/usr/bin/env python3
from utils import BaseSolution

"""Return a list of pairs (x_change, y_change [challenge 1] | aim_change [challenge 2])"""
def get_moves(ll):
    moves = []
    for l in ll:
        size = int(l.split(' ')[1])
        if l.startswith('forward'):
            moves.append((size, 0))
        elif l.startswith('down'):
            moves.append((0, size))
        else:
            moves.append((0, 0 - size))

    return moves

class Solution(BaseSolution):
    def part1(self, ll) -> str:
        moves = get_moves(ll)

        x, y = 0, 0
        for x_change, y_change in moves:
            x += x_change
            y += y_change
        return str(x * y)

    def part2(self, ll) -> str:
        moves = get_moves(ll)

        x, y, aim = 0, 0, 0
        for x_change, aim_change in moves:
            if x_change:
                x += x_change
                y += aim * x_change
            else:
                aim += aim_change

        return str(x * y)

if __name__ == '__main__':
    Solution()
