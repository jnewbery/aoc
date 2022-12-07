#!/usr/bin/env python3
import argparse
import importlib

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--day",  type=int, help="Advent of code day")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument("-p", "--part", type=int, help="Which part to run. Leave blank to run both parts")

    args = parser.parse_args()

    day = f"{args.day:02}"
    if not args.part:
        parts = [1, 2]
    else:
        parts = [args.part]

    print(f"day: {day}")
    print(f"test: {args.test}")
    print(f"parts: {parts}")

    mod = importlib.import_module(f"{day}")

    if args.test:
        ll = mod.TEST_INPUT.splitlines()
    else:
        f = open(f"{day}.txt", 'r')
        ll = f.read().splitlines()

    if 1 in parts:
        sol1 = mod.part1(ll)
        print(f"Part1 : {sol1}")
        if args.test:
            assert(sol1 == mod.TEST_SOL[0])

    if 2 in parts:
        sol2 = mod.part2(ll)
        print(f"Part2 : {sol2}")
        if args.test:
            assert(sol2 == mod.TEST_SOL[1])

if __name__ == "__main__":
    main()
