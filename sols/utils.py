import argparse
import enum
from functools import wraps
import os
from pathlib import Path
import sys
import time

class EXIT_CODES(enum.Enum):
    SUCCESS = 0
    NOT_IMPLEMENTED = 38

def exit_not_implemented():
    sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        ret = func(*args, **kwargs)
        end = time.time_ns()
        execution_time = end - start
        return {"solution": str(ret), "execution_time": f"{int(execution_time // 1e6)}ms"}
    return wrapper

def get_params(sol_file: str) -> argparse.Namespace:
    """Get the part and input"""
    parser = argparse.ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    parser.add_argument("-t", "--test", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print solution and extra information")

    args = parser.parse_args()

    parent_dir = Path(sol_file).parent
    puzzle_stem = Path(sol_file).stem

    if args.test:
        input_file_stem = f"{parent_dir}/{puzzle_stem}_test_input"
    else:
        input_file_stem = f"{parent_dir}/{puzzle_stem}_input"
    
    if os.path.exists(f"{input_file_stem}{args.part}.txt"):
        input_file = f"{input_file_stem}{args.part}.txt"
    else:
        input_file = f"{input_file_stem}.txt"

    with open(input_file) as f:
        args.puzzle_input = f.read()

    return args

class Solution:
    @time_execution
    def part1(self, ll):
        exit_not_implemented()

    def part2(self, ll):
        exit_not_implemented()

    def run(self, sol_file: str):
        args = get_params(sol_file)

        start = time.time_ns()
        func = getattr(self, f"part{args.part}")
        sol = func(args.puzzle_input.splitlines())
        end = time.time_ns()
        execution_time = end - start
        if args.verbose:
            print({"solution": str(sol), "execution_time": f"{int(execution_time // 1e6)}ms"})
        else:
            print(str(sol))
