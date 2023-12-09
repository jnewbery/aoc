#!/usr/bin/env python3
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

def part1(ll):
    moves = get_moves(ll)

    x, y = 0, 0
    for x_change, y_change in moves:
        x += x_change
        y += y_change
    return x * y

def part2(ll):
    moves = get_moves(ll)

    x, y, aim = 0, 0, 0
    for x_change, aim_change in moves:
        if x_change:
            x += x_change
            y += aim * x_change
        else:
            aim += aim_change

    return x * y

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

TEST_SOL = [150, 900]

FULL_INPUT = """forward 5
down 8
down 6
down 7
down 8
forward 7
down 3
up 6
forward 6
down 2
forward 5
down 6
up 3
down 4
forward 4
down 6
down 1
up 5
forward 5
down 1
down 7
up 2
down 7
forward 1
forward 6
down 1
up 1
up 4
forward 3
forward 6
forward 1
forward 4
up 3
forward 1
forward 4
down 9
forward 4
forward 8
up 8
forward 5
up 4
up 3
down 8
forward 5
down 4
forward 1
forward 7
down 1
forward 8
down 4
forward 2
forward 7
forward 9
up 4
down 3
forward 7
forward 6
down 8
forward 2
forward 5
forward 4
down 6
forward 6
up 5
down 3
down 6
down 5
down 7
down 8
up 5
down 5
forward 5
forward 4
up 3
down 7
down 3
forward 4
down 2
forward 4
forward 3
forward 4
forward 9
forward 6
forward 8
up 8
down 8
up 5
down 4
down 8
up 7
up 8
down 6
down 3
forward 2
forward 7
up 1
up 2
forward 2
down 7
down 1
up 9
forward 6
forward 4
down 2
up 6
down 2
down 1
down 3
up 6
down 1
down 8
forward 7
up 8
forward 5
forward 8
down 8
forward 6
forward 8
down 3
down 4
down 6
up 2
forward 6
up 9
forward 4
forward 8
up 4
down 8
forward 8
down 8
down 4
down 5
forward 7
down 6
down 6
up 2
up 1
forward 7
forward 8
forward 4
forward 9
down 7
forward 4
up 5
down 3
up 4
down 9
down 2
down 8
forward 3
forward 5
forward 7
forward 9
forward 5
forward 8
forward 6
forward 4
forward 6
forward 7
forward 2
down 1
down 8
down 4
down 5
down 6
up 3
up 2
forward 4
down 4
forward 7
up 6
up 9
down 1
down 3
down 1
up 3
up 1
down 2
up 5
forward 1
down 7
forward 9
down 4
up 4
down 6
down 3
forward 4
up 6
up 4
forward 1
up 7
down 1
down 7
down 7
forward 9
down 3
down 3
forward 6
down 2
forward 7
up 4
up 8
down 8
forward 7
forward 6
down 7
forward 5
up 6
up 6
down 9
up 6
up 2
forward 9
forward 1
up 5
up 3
down 9
up 8
down 7
up 7
forward 5
down 7
down 4
forward 2
forward 3
forward 5
down 1
up 6
down 6
up 6
down 8
down 3
down 4
forward 9
down 3
forward 3
up 1
down 2
forward 8
down 7
up 9
forward 1
down 3
forward 1
forward 8
down 3
forward 8
forward 6
down 1
down 9
forward 2
down 1
down 6
up 1
up 7
down 9
forward 6
forward 5
forward 2
up 6
down 6
forward 6
up 3
down 7
down 8
forward 5
down 7
forward 8
down 8
forward 4
down 6
forward 4
down 7
up 5
down 5
down 5
down 4
down 3
forward 8
forward 1
down 8
down 2
forward 3
forward 7
forward 3
down 5
down 6
down 8
down 6
forward 9
forward 4
forward 8
down 5
down 7
forward 4
up 5
down 8
up 6
up 7
down 6
down 8
forward 3
up 6
forward 7
down 4
up 1
up 8
forward 3
down 6
down 1
forward 7
down 1
down 9
forward 6
down 4
forward 3
forward 1
down 5
down 9
down 9
down 5
down 8
down 7
forward 1
forward 5
down 2
forward 2
forward 1
down 8
forward 6
down 3
forward 4
up 2
up 8
forward 7
forward 4
down 8
up 6
forward 3
up 1
up 2
forward 5
forward 9
down 5
forward 2
forward 5
up 6
down 1
down 1
down 6
forward 6
down 7
forward 5
forward 8
down 7
down 5
forward 9
forward 1
up 6
down 7
forward 1
forward 4
down 5
down 6
up 3
up 8
up 5
down 8
down 8
down 6
down 2
down 3
down 9
forward 8
forward 7
forward 7
up 5
down 5
forward 9
up 8
up 5
forward 1
down 9
down 9
forward 9
forward 4
forward 6
up 9
up 5
up 3
down 9
up 7
up 1
down 3
down 9
down 7
forward 6
down 7
forward 7
forward 8
down 2
forward 5
up 1
down 6
up 9
forward 5
up 9
down 2
down 3
forward 5
down 9
forward 9
forward 2
forward 8
down 1
forward 8
up 1
forward 3
up 1
down 1
forward 9
down 2
forward 2
up 1
up 8
down 2
down 7
down 5
up 2
up 6
down 9
down 7
down 7
up 6
up 8
down 7
forward 5
down 4
down 5
up 8
up 6
down 6
forward 6
up 6
down 1
down 1
down 1
forward 1
down 8
down 4
down 5
down 2
down 5
up 8
up 8
down 3
down 6
down 1
forward 6
forward 5
forward 1
down 3
down 4
up 9
down 3
up 8
forward 5
down 5
forward 2
down 8
down 2
up 1
forward 7
up 8
forward 7
down 3
down 1
down 3
forward 4
down 5
down 8
forward 8
forward 3
forward 7
down 7
forward 4
down 1
forward 3
up 2
down 7
down 1
forward 4
forward 7
down 3
down 1
forward 4
down 3
forward 2
up 9
down 5
down 9
forward 5
up 5
down 3
up 6
up 8
down 7
down 3
down 9
forward 6
forward 8
forward 3
down 6
up 8
forward 8
forward 9
down 4
down 1
forward 2
down 2
up 2
down 5
down 1
down 3
forward 4
down 3
up 8
up 6
up 5
down 4
forward 3
up 6
forward 6
forward 2
down 8
down 5
forward 3
up 1
forward 5
forward 9
forward 5
down 5
forward 3
forward 6
forward 5
forward 3
down 1
down 1
down 1
down 9
forward 8
forward 2
forward 4
forward 8
down 1
up 8
down 1
down 6
down 5
up 8
down 4
forward 8
forward 6
down 6
forward 2
forward 7
forward 2
up 7
forward 4
up 1
up 8
down 3
down 2
down 3
up 7
down 9
up 5
down 1
down 3
up 5
down 6
up 9
down 4
down 7
down 6
down 4
forward 5
forward 6
down 8
forward 3
forward 8
up 5
up 6
up 8
forward 8
forward 1
down 6
forward 3
forward 3
forward 6
down 3
down 2
forward 5
down 5
forward 6
down 3
down 9
down 8
down 6
down 6
forward 1
up 5
down 9
forward 3
forward 3
down 2
forward 8
forward 3
forward 2
forward 5
down 4
down 1
up 2
down 1
down 1
forward 5
down 7
up 7
down 9
down 8
down 6
forward 3
forward 5
down 3
down 6
up 3
up 2
up 8
down 3
up 3
down 6
forward 7
forward 4
up 5
forward 1
up 3
forward 8
down 2
down 5
down 2
forward 4
forward 4
down 4
up 8
down 1
up 2
forward 2
forward 9
forward 4
down 3
down 7
forward 1
down 2
forward 8
down 8
forward 3
down 7
forward 9
forward 6
up 1
forward 3
up 2
up 3
forward 6
down 8
up 9
down 2
down 9
down 6
down 4
forward 5
forward 3
up 7
forward 7
up 7
up 6
down 7
down 2
up 7
down 5
up 9
forward 3
up 6
up 6
up 6
up 1
forward 5
forward 5
down 8
forward 6
forward 7
down 3
down 4
down 2
down 4
down 1
forward 7
down 7
down 5
forward 8
up 6
up 8
forward 8
forward 2
forward 4
down 6
down 4
down 2
down 3
forward 8
forward 6
down 3
forward 7
forward 4
up 8
down 9
forward 5
up 5
up 5
up 7
forward 3
up 1
down 2
forward 5
forward 5
up 1
forward 4
down 6
up 5
up 3
forward 9
down 9
down 6
down 1
down 2
down 4
down 7
forward 3
up 5
forward 2
down 3
forward 7
up 8
up 3
forward 6
up 7
up 1
up 2
down 5
forward 5
down 3
down 5
down 6
up 1
down 2
up 1
forward 3
down 3
down 4
down 6
down 1
down 3
forward 9
forward 1
down 1
up 3
forward 4
forward 7
forward 4
down 2
forward 6
forward 2
forward 7
down 9
forward 8
forward 3
up 8
down 9
up 8
forward 5
forward 9
down 4
forward 1
up 9
forward 2
down 6
up 3
forward 1
forward 3
forward 8
down 7
down 3
down 5
down 2
down 2
forward 4
forward 1
down 2
up 8
down 2
forward 3
down 2
down 6
down 1
up 1
down 7
down 3
forward 3
forward 1
forward 9
down 9
down 2
up 1
forward 9
up 2
down 2
forward 3
down 4
forward 9
forward 5
up 5
forward 2
up 3
forward 8
down 3
forward 5
forward 5
down 8
up 9
forward 7
up 2
up 2
up 1
up 7
down 8
forward 9
forward 9
up 6
down 5
forward 7
down 9
down 8
down 5
down 3
down 2
forward 6
down 7
forward 3
up 5
forward 1
up 7
forward 3
down 5
down 9
down 8
forward 2
up 4
forward 7
forward 5
forward 8
forward 7
up 7
forward 4
up 7
down 9
forward 1
forward 3
down 3
forward 4
down 3
forward 3
down 5
down 1
forward 6
down 4
down 3
down 2
up 1
down 1
down 6
down 6
forward 9
down 5
forward 1
up 4
forward 7
down 8
forward 1
forward 9
forward 7
down 1
down 3
up 2
down 5
up 6
forward 2
up 2
down 7
down 9
forward 3
up 5
up 7
down 4
forward 6
down 8
forward 7
up 1
up 4
forward 4
down 9
forward 9
forward 9
down 3
forward 5
forward 1
down 3
down 8
forward 7
down 4
forward 3
down 3
forward 8
forward 2
forward 6
up 9
forward 2
down 9
forward 2
down 1
forward 9
up 1
up 4
up 1
down 1
forward 4
up 9
up 8
down 1
down 3
down 2
forward 9
down 7
down 4
forward 2
up 9
down 7
down 1
down 9
forward 2
down 2
forward 9
down 5
up 1
down 3
up 6
down 4
forward 8
down 2
down 2
down 9
forward 9
forward 2
down 1
forward 6
down 2
up 4
down 8
up 4
down 6
down 2
forward 7
down 3
up 3
forward 1
up 4
forward 5
down 7
down 8
forward 7
forward 3
down 5
up 6
down 7
down 1
up 7
down 1
forward 6
forward 3
forward 3
forward 7"""

FULL_SOL = [1660158, 1604592846]
