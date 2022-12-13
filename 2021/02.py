#!/usr/bin/env python3

def main():
    moves = read_file('input.txt')

    print(sol1(moves))
    print(sol2(moves))

"""Return a list of pairs (x_change, y_change [challenge 1] | aim_change [challenge 2])"""
def read_file(filename):
    moves = []
    with open(filename, 'r') as f:
        for l in f.readlines():
            size = int(l.split(' ')[1])
            if l.startswith('forward'):
                moves.append((size, 0))
            elif l.startswith('down'):
                moves.append((0, size))
            else:
                moves.append((0, 0 - size))

    return moves

def sol1(moves):
    x, y = 0, 0
    for x_change, y_change in moves:
        x += x_change
        y += y_change
    return x * y

def sol2(moves):
    x, y, aim = 0, 0, 0
    for x_change, aim_change in moves:
        if x_change:
            x += x_change
            y += aim * x_change
        else:
            aim += aim_change

    return x * y

if __name__ == "__main__":
    main()
