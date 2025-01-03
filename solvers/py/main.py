#!/usr/bin/env python3
import argparse
import enum
import os
import sys
import importlib
import time
from pathlib import Path
import json

class EXIT_CODES(enum.Enum):
    SUCCESS = 0
    NOT_IMPLEMENTED = 38

def get_puzzle_input(puzzle: str, test: bool) -> list[str]:
    if test:
        input_dir = Path(__file__).parent.parent.parent / "inputs" / "test"
    else:
        input_dir = Path(__file__).parent.parent.parent / "inputs" / "full"

    if os.path.exists(input_dir / f"{puzzle[0:6]}_{puzzle[6]}.txt"):
        input_file = input_dir / f"{puzzle[0:6]}_{puzzle[6]}.txt"
    else:
        input_file = input_dir / f"{puzzle[0:6]}.txt"

    with open(input_file) as f:
        return f.read().splitlines()

def main(puzzle: str, test: bool, verbose: bool) -> None:
    if not os.path.exists(Path(__file__).parent / f"{puzzle[:6]}.py"):
        print(f"{puzzle}.py not found")
        sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

    puzzle_input = get_puzzle_input(puzzle, test)
    solver = importlib.import_module(puzzle[:6]).Solution()
    start = time.time_ns()
    func = getattr(solver, f"part{puzzle[6]}")
    try:
        sol = func(puzzle_input)
    except NotImplementedError:
        sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

    execution_time = time.time_ns() - start
    if verbose:
        print(json.dumps({"solution": str(sol), "execution_time": f"{int(execution_time // 1e3)}"}))
    else:
        print(str(sol))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("puzzle", help="Which puzzle to run, in format YYYYDDP.")
    parser.add_argument("-t", "--test", action="store_true", default=False, help="Run solver on test input. Defaults to false")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Print solution and execution information as JSON. Defaults to false")

    args = parser.parse_args()

    if len(args.puzzle) != 7:
        print("Puzzle must be in format YYYYDDP.")
        sys.exit(1)

    main(args.puzzle, args.test, args.verbose)
