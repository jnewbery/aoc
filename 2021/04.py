#!/usr/bin/env python3

TEST_INPUT="""13,47,64,52,60,69,80,85,57,1,2,6,30,81,86,40,27,26,97,77,70,92,43,94,8,78,3,88,93,17,55,49,32,59,51,28,33,41,83,67,11,91,53,36,96,7,34,79,98,72,39,56,31,75,82,62,99,66,29,58,9,50,54,12,45,68,4,46,38,21,24,18,44,48,16,61,19,0,90,35,65,37,73,20,22,89,42,23,15,87,74,10,71,25,14,76,84,5,63,95

88 67 20 19 15
22 76 86 44 73
 7 42  6 69 25
12 68 92 21 75
97 45 13 52 70

75 98 24 18 77
17 93 46 49 13
92 56 97 57 66
44  0 65 54 74
23  6 53 42 20

92 94  9 27 41
73 28 62 90 40
78  3 12 37 32
 8 86 91 16 30
84 38 68 11 19
"""

class Board:
    def __init__(self, numbers):
        """Takes a list of lists of numbers"""
        self.rows = []
        for row in numbers:
            self.rows.append([int(n) for n in row.split(" ") if n])
        self.columns = [list(c) for c in zip(*self.rows)]

    def draw(self, number):
        for row in self.rows:
            if number in row:
                row.remove(number)
                if not row:
                    return number * sum([sum(row) for row in self.rows])

        for column in self.columns:
            if number in column:
                column.remove(number)
                if not column:
                    return number * sum([sum(column) for column in self.columns])

        return False

def parse_input(lines):
    draws = [int(d) for d in lines.pop(0).split(',')]
    nonempty = [l for l in lines if l]
    boards = [Board(nonempty[i:i + 5]) for i in range(0, len(nonempty), 5)]

    return draws, boards

def sol1(draws, boards):
    for d in draws:
        for b in boards:
            ret = b.draw(d)
            if ret:
                return ret

def sol2(draws, boards):
    num_boards = len(boards)
    for d in draws:
        for i, b in enumerate(boards):
            if not b:
                continue
            ret = b.draw(d)
            if ret:
                # print(f"board {101 - num_boards} complete!")
                if num_boards == 1:
                    # print(b)
                    return ret
                boards[i] = None
                num_boards -= 1

def main():
    test_draws, test_boards = parse_input(TEST_INPUT.splitlines())

    print(f"test sol1 = {sol1(test_draws, test_boards)}")
    print(f"test sol2 = {sol2(test_draws, test_boards)}")

    draws, boards = parse_input([l.strip() for l in open("input.txt", "r").readlines()])

    print(f"sol1 = {sol1(draws, boards)}")
    print(f"sol2 = {sol2(draws, boards)}")

if __name__ == "__main__":
    main()
