#!/usr/bin/env python3
import argparse
import importlib

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--day",  type=int, help="Advent of code day")
    parser.add_argument("-e", "--example", action="store_true", help="Whether to run the example")

    args = parser.parse_args()

    day = f"{args.day:02}"

    print(f"day:", day)
    print(f"example:", args.example)

    mod = importlib.import_module(f"{day}")

    if args.example:
        ll = mod.EXAMPLE.splitlines()
    else:
        f = open(f"{day}.txt", 'r')
        ll = f.read().splitlines()

    sol1 = mod.part1(ll)
    print(f"Part1 : {sol1}")
    if args.example:
        assert(sol1 == mod.EXAMPLE_SOL[0])

    sol2 = mod.part2(ll)
    print(f"Part2 : {sol2}")
    if args.example:
        assert(sol2 == mod.EXAMPLE_SOL[1])

if __name__ == "__main__":
    main()
