#!/usr/bin/env python3

def read_file(filename):
    with open(filename, 'r') as f:
        for l in f.readlines():
            yield list(l.strip())

"""Normalize 1 -> 1 , 0 -> -1"""
def norm1(n):
    return 2 * int(n) - 1

"""Normalize +ve -> 1, -ve -> 0"""
def norm2(n):
    assert n != 0
    return ((n // abs(n)) + 1) // 2

def sol1(lines):
    normed_lines = list([map(norm1, l) for l in lines])
    line_len = len(lines[0])
    columns = list(sum(l) for l in zip(*normed_lines))
    gamma_list = list(map(norm2, columns))

    gamma = 0
    for i, d in enumerate(reversed(gamma_list)):
        gamma += d * 2**i

    epsilon = 2 ** line_len - 1 - gamma

    return gamma * epsilon

class Node:
    def __init__(self):
        self.count = 0
        self.zeros = None
        self.ones = None

    def store(self, line, number):
        self.count += 1
        if line:
            left_bit = line.pop(0)
            if not self.zeros:
                # Always initialize both children
                assert not self.ones
                self.zeros = Node()
                self.ones = Node()
            if left_bit == '0':
                self.zeros.store(line, number)
            else:
                self.ones.store(line, number)

    """02 rating => mode == True, co2 rating => mode == False"""
    def rating(self, mode):
        node = self
        number = 0
        while node.zeros:
            number *= 2
            assert node.ones
            assert node.zeros.count or node.ones.count
            if not node.zeros.count or (node.ones.count and (node.zeros.count <= node.ones.count) == mode):
                number += 1
                node = node.ones
            else:
                node = node.zeros
        return number

def sol2(lines):
    root = Node()
    for line in lines:
        number = int(''.join(line), 2)
        root.store(line, number)

    o2 = root.rating(True)
    co2 = root.rating(False)
    
    return o2 * co2

def main():
    lines = list(read_file('input.txt'))

    print(f"sol1 = {sol1(lines)}")
    print(f"sol2 = {sol2(lines)}")

if __name__ == "__main__":
    main()
