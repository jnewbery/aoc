#!/usr/bin/env python3
import hashlib
def register_generator(ll):
    reg = 1
    yield reg
    for l in ll:
        match l.split():
            case ['noop']:
                yield reg
            case 'addx', size:
                yield reg
                reg += int(size)
                yield reg

def part1(ll):
    # print([(i,n) for i,n in enumerate(register_generator(ll))])
    # print([((i+1), n) for i,n in enumerate(register_generator(ll)) if i in range(19, 220, 40)])
    return sum(((i+1) * n for i, n in enumerate(register_generator(ll)) if i in range(19, 220, 40)))

def part2(ll):
    screen = ''
    for (t, x) in enumerate(register_generator(ll)):
        # print(x)
        if not t % 40 and t > 0:
            screen += '\n'
        if abs((t % 40) - x) <= 1:
            screen += '#'
        else:
            screen += '.'

    # The solution is a string rendering of an image, so return
    # the hash to check correctness.
    return hashlib.sha256(screen.encode("utf-8")).hexdigest()[0:8]

TEST_INPUT = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

TEST_SOL = [13140, "67702651"]

FULL_INPUT = """noop
noop
noop
addx 6
addx -1
addx 5
noop
noop
noop
addx 5
addx -8
addx 9
addx 3
addx 2
addx 4
addx 3
noop
addx 2
noop
addx 1
addx 6
noop
noop
noop
addx -39
noop
addx 5
addx 2
addx -2
addx 3
addx 2
addx 5
addx 2
addx 2
addx 13
addx -12
noop
addx 7
noop
addx 2
addx 3
noop
addx -25
addx 30
addx -10
addx 13
addx -40
noop
addx 5
addx 2
addx 3
noop
addx 2
addx 3
addx -2
addx 3
addx -1
addx 7
noop
noop
addx 5
addx -1
addx 6
noop
noop
noop
noop
addx 9
noop
addx -1
noop
addx -39
addx 2
addx 33
addx -29
addx 1
noop
addx 4
noop
noop
noop
addx 3
addx 2
noop
addx 3
noop
noop
addx 7
addx 2
addx 3
addx -2
noop
addx -30
noop
addx 40
addx -2
addx -38
noop
noop
noop
addx 5
addx 5
addx 2
addx -9
addx 5
addx 7
addx 2
addx 5
addx -18
addx 28
addx -7
addx 2
addx 5
addx -28
addx 34
addx -3
noop
addx 3
addx -38
addx 10
addx -3
addx 29
addx -28
addx 2
noop
noop
noop
addx 5
noop
addx 3
addx 2
addx 7
noop
addx -2
addx 5
addx 2
noop
addx 1
addx 5
noop
noop
addx -25
noop
noop"""

FULL_SOL = [14060, "9e9c7512"]
