import argparse
import enum
import json
import os
from pathlib import Path
import re
import sys
import time

class EXIT_CODES(enum.Enum):
    SUCCESS = 0
    NOT_IMPLEMENTED = 38

def exit_not_implemented():
    sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

class BaseSolution:
    def part1(self, ll: list[str]) -> str:
        del ll
        raise NotImplementedError

    def part2(self, ll: list[str]) -> str:
        del ll
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
        assert self.sol_file is not None
        if self.test:
            input_dir = Path(self.sol_file).parent.parent.parent / "inputs" / "test"
        else:
            input_dir = Path(self.sol_file).parent.parent.parent / "inputs" / "full"

        puzzle_stem = Path(self.sol_file).stem

        if os.path.exists(input_dir / f"{puzzle_stem}_{self.part}.txt"):
            input_file = input_dir / f"{puzzle_stem}_{self.part}.txt"
        else:
            input_file = input_dir / f"{puzzle_stem}.txt"

        with open(input_file) as f:
            self.puzzle_input = f.read().splitlines()

    def __init__(self):
        self.sol_file = sys.modules[self.__module__].__file__
        self.get_params()
        self.get_puzzle_input()

        start = time.time_ns()
        func = getattr(self, f"part{self.part}")

        sol = None
        try:
            sol = func(self.puzzle_input)
        except NotImplementedError:
            self.exit_not_implemented()

        execution_time = time.time_ns() - start

        if self.verbose:
            print(json.dumps({"solution": str(sol), "execution_time": f"{int(execution_time // 1e6)}ms"}))
        else:
            print(str(sol))

    def exit_not_implemented(self) -> None:
        sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

def get_numbers(line: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", line)]
