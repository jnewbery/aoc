import enum
import re
import sys

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

    def __init__(self):
        pass

    def exit_not_implemented(self) -> None:
        sys.exit(EXIT_CODES.NOT_IMPLEMENTED.value)

def get_numbers(line: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", line)]
