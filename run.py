#!/usr/bin/env python3
import argparse
import importlib
import os
import re

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--day",  type=int, help="Advent of code day. Leave blank to run all days.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument("-p", "--part", type=int, help="Which part to run. Leave blank to run both parts.")

    args = parser.parse_args()

    if not args.day:
        regex = re.compile(r"^\d{2}\.py$")
        days = sorted([f[0:2] for f in os.listdir() if regex.match(f)])
    else:
        days = [f"{args.day:02}"]

    if not args.part:
        parts = [1, 2]
    else:
        parts = [args.part]

    print(f"days: {days}")
    print(f"test: {args.test}")
    print(f"parts: {parts}")

    for day in days:
        mod = importlib.import_module(f"{day}")

        if args.test:
            ll = mod.TEST_INPUT.splitlines()
        else:
            ll = mod.FULL_INPUT.splitlines()

        for part in parts:
            func = getattr(mod, f"part{part}")
            try:
                sol = func(ll.copy())
                print(f"Part{part} : {sol}")
                if args.test:
                    assert(sol == mod.TEST_SOL[part - 1])
            except NotImplementedError:
                print("Not implemented yet!")

if __name__ == "__main__":
    main()
