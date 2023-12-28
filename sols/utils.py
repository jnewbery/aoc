import argparse
import enum
import json
import os
from pathlib import Path
import sys
import time

class EXIT_CODES(enum.Enum):
    SUCCESS = 0
    NOT_IMPLEMENTED = 38

def exit_not_implemented():
    sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

class BaseSolution:
    def part1(self, ll) -> str:
        raise NotImplementedError

    def part2(self, ll) -> str:
        raise NotImplementedError

    def get_params(self):
        """Get the part and input"""
        parser = argparse.ArgumentParser()
        parser.add_argument("part", choices=["1", "2"])
        parser.add_argument("-t", "--test", action="store_true")
        parser.add_argument("-v", "--verbose", action="store_true", help="Print solution and extra information")

        args = parser.parse_args()

        self.part = args.part
        self.test = args.test
        self.verbose = args.verbose

    def get_puzzle_input(self):
        parent_dir = Path(self.sol_file).parent
        puzzle_stem = Path(self.sol_file).stem

        if self.test:
            input_file_stem = f"{parent_dir}/{puzzle_stem}_test_input"
        else:
            input_file_stem = f"{parent_dir}/{puzzle_stem}_input"
        
        if os.path.exists(f"{input_file_stem}{self.part}.txt"):
            input_file = f"{input_file_stem}{self.part}.txt"
        else:
            input_file = f"{input_file_stem}.txt"

        with open(input_file) as f:
            self.puzzle_input = f.read().splitlines()

    def __init__(self):
        self.sol_file = sys.modules[self.__module__].__file__
        self.get_params()
        self.get_puzzle_input()

        start = time.time_ns()
        func = getattr(self, f"part{self.part}")

        try:
            sol = func(self.puzzle_input)
        except NotImplementedError:
            exit_not_implemented()

        execution_time = time.time_ns() - start

        if self.verbose:
            print(json.dumps({"solution": str(sol), "execution_time": f"{int(execution_time // 1e6)}ms"}))
        else:
            print(str(sol))
