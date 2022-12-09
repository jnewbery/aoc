#!/usr/bin/env python3
import argparse
import importlib
import os
import re

from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--args",  action="store_true", help="Print args")
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

    if args.args:
        print(f"days: {days}")
        print(f"test: {args.test}")
        print(f"parts: {parts}")

    results = []
    for day in days:
        result = {'Day': f'Day {day}'}
        mod = importlib.import_module(f"{day}")

        if args.test:
            ll = mod.TEST_INPUT.splitlines()
        else:
            ll = mod.FULL_INPUT.splitlines()

        for part in parts:
            func = getattr(mod, f"part{part}")
            try:
                sol = func(ll.copy())
                result[f"Part {part}"] = sol
                if args.test:
                    assert(sol == mod.TEST_SOL[part - 1])
            except NotImplementedError:
                result[f'Part {part}'] = "Not implemented"

        results.append(result)

    print(tabulate(results, headers='keys', tablefmt="github"))

if __name__ == "__main__":
    main()
