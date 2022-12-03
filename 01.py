#!/usr/bin/env python3

def main():
    totals = [0]
    with open('01.txt', 'r') as f:
        for l in f.readlines():
            if l == "\n":
                totals.append(0)
            else:
                totals[-1] += int(l)
    totals.sort()
    print(f"Part 1: {totals[-1]}")
    print(f"Part 2: {sum(totals[-3:])}")

if __name__ == "__main__":
    main()
