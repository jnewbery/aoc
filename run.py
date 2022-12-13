#!/usr/bin/env python3
import argparse
import importlib
import os
import re

from tabulate import tabulate

if os.name == 'posix':
    GREEN = "\033[0;32m"
    RED = "\033[1;31m"
    BLUE = "\033[0;34m"
    RESET = "\033[0;0m"
else:
    GREEN = ""
    RED = ""
    BLUE = ""
    RESET = ""

def success(string):
    return GREEN + str(string) + RESET

def failure(string):
    return RED + str(string) + RESET

def inconclusive(string):
    return BLUE + str(string) + RESET

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--args",  action="store_true", help="Print args")
    parser.add_argument("-d", "--day",  type=int, help="Advent of code day. Leave blank to run all days.")
    parser.add_argument("-t", "--test", action="store_true", help="Whether to run with test input. If false, runs with full input.")
    parser.add_argument("-p", "--part", type=int, help="Which part to run. Leave blank to run both parts.")
    parser.add_argument("-y", "--year", type=int, help="Which year to run.")

    args = parser.parse_args()

    if not args.day:
        regex = re.compile(r"^\d{2}\.py$")
        days = sorted([f[0:2] for f in os.listdir(str(args.year)) if regex.match(f)])
    else:
        days = [f"{args.day:02}"]

    if not args.part:
        parts = [1, 2]
    else:
        parts = [args.part]

    if args.args:
        print(f"year: {args.year}")
        print(f"days: {days}")
        print(f"test: {args.test}")
        print(f"parts: {parts}")

    results = []
    for day in days:
        result = {'Day': f'Day {day}'}
        mod = importlib.import_module(f"{args.year}.{day}")

        if args.test:
            ll = mod.TEST_INPUT.splitlines()
        else:
            ll = mod.FULL_INPUT.splitlines()

        for part in parts:
            func = getattr(mod, f"part{part}")
            input_str = "test input" if args.test else "full input"
            result_header = f"Part {part} ({input_str})"
            try:
                sol = func(ll.copy())
                sols = mod.TEST_SOL if args.test else mod.FULL_SOL
                if len(sols) < part:
                    result[result_header] = inconclusive(sol)
                elif sols[part - 1] == sol:
                    result[result_header] = success(sol)
                else:
                    result[result_header] = failure(sol)
            except NotImplementedError:
                result[result_header] = inconclusive("Not implemented")

        results.append(result)

    print(tabulate(results, headers='keys', tablefmt="github"))

if __name__ == "__main__":
    main()
