#!/usr/bin/env python3

def main():
    lines = list(read_file('input.txt'))
    print(sol1(lines))

"""Normalize 1 -> 1 , 0 -> -1"""
def norm1(n):
    return 2 * n - 1

"""Normalize +ve -> 1, -ve -> 0"""
def norm2(n):
    assert n != 0
    return ((n // abs(n)) + 1) // 2

def read_file(filename):
    with open(filename, 'r') as f:
        for l in f.readlines():
            yield(list(map(norm1, [int(d) for d in l.rstrip("\n")])))

def sol1(lines):
    line_len = len(lines[0])
    columns = list(sum(l) for l in zip(*lines))
    gamma_list = list(map(norm2, [sum(l) for l in zip(*lines)]))

    print(lines)
    print(columns)
    print(gamma_list)
    gamma = 0
    for i, d in enumerate(reversed(gamma_list)):
        gamma += d * 2**i
        print(i, d)

    print(gamma)

    epsilon = 2 ** line_len - 1 - gamma

    print(epsilon)

    return gamma * epsilon


if __name__ == "__main__":
    main()
