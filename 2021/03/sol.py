#!/usr/bin/env python3

class Node:
    def __init__(self):
        self.count = 0
        self.zeros = None
        self.ones = None

        self.number = None

    def store(self, line, number):
        self.count += 1
        if line:
            left_digit = line.pop(0)
            if not self.zeros:
                self.zeros = Node()
            if not self.ones:
                self.ones = Node()
            if left_digit == '0':
                self.zeros.store(line, number)
            else:
                self.ones.store(line, number)
        else:
            self.number = number

    """02 rating => mode == True, co2 rating => mode == False"""
    def rating(self, mode):
        node = self
        while node.zeros:
            assert node.ones
            if mode:
                print("o2_debug", node.count, node.zeros.count, node.ones.count)
                if node.zeros.count > node.ones.count:
                    # most common value if equal keep 1
                    node = node.zeros
                else:
                    node = node.ones
            else:
                print("co2_debug", node.count, node.zeros.count, node.ones.count)
                # lest common if equal pick 0
                if node.zeros.count == 1:
                    node = node.zeros
                elif node.ones.count == 1:
                    # ones must be lowest
                    node = node.ones
                elif node.zeros.count and node.zeros.count <= node.ones.count:
                    node = node.zeros
                else:
                    node = node.ones
        return node.number

def main():
    lines = list(read_file('input.txt'))

    root = Node()
    for line in lines:
        number = int(''.join(line), 2)
        root.store(line, number)

    o2 = root.rating(True)
    print("o2 rating", o2)
    co2 = root.rating(False)
    print("co2 rating", co2)
    print(o2 * co2)
    import pdb;pdb.set_trace()
    # print(sol1(lines))

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
            yield list(l.strip())

# def sol1(lines):
#     print(lines)
#     normed_lines = list(map(norm1, lines))
#     line_len = len(lines[0])
#     columns = list(sum(l) for l in zip(*normed_lines))
#     gamma_list = list(map(norm2, columns))

#     # print(lines)
#     # print(columns)
#     # print(gamma_list)
#     gamma = 0
#     for i, d in enumerate(reversed(gamma_list)):
#         gamma += d * 2**i

#     # print(gamma)

#     epsilon = 2 ** line_len - 1 - gamma

#     # print(epsilon)

#     return gamma * epsilon

if __name__ == "__main__":
    main()
