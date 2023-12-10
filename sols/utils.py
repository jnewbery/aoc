import argparse
import enum
import os
from pathlib import Path
import sys

class EXIT_CODES(enum.Enum):
    SUCCESS = 0
    NOT_IMPLEMENTED = 38

def exit_not_implemented():
    sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

def get_params(sol_file: str) -> tuple[str, str]:
    """Get the part and input"""
    parser = argparse.ArgumentParser()
    parser.add_argument("part", choices=["1", "2"])
    parser.add_argument("-t", "--test", action="store_true")

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
        return args.part, f.read()
