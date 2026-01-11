from utils import exit_not_implemented
from dataclasses import dataclass
import operator
from typing import Callable

@dataclass
class Monkey():
    left: str | int | None
    right: str | int | None
    num: int | None
    operation: None | Callable

    def __init__(self, l: str):
        parts = l.split()
        if len(parts) == 1:
            self.left = None
            self.right = None
            self.operation = None
            self.num = int(parts[0])
        else:
            self.num = None
            self.left = parts[0]
            self.right = parts[2]

            match parts[1]:
                case "+":
                    self.operation = operator.add
                case "-":
                    self.operation = operator.sub
                case "*":
                    self.operation = operator.mul
                case "/":
                    self.operation = operator.floordiv

    def val(self, monkeys: dict[str, Monkey]) -> int:
        if self.num is not None:
            return self.num
        assert self.operation
        assert type(self.left) == str
        assert type(self.right) == str
        return self.operation(monkeys[self.left].val(monkeys), monkeys[self.right].val(monkeys))


def part1(ll: list[str], args=None) -> str:
    del args

    monkeys: dict[str, Monkey] = {}
    for l in ll:
        name, monkey = l.split(": ")
        monkeys[name] = Monkey(monkey)

    return str(monkeys["root"].val(monkeys))

def part2(ll: list[str], args=None) -> str:
    del args
    exit_not_implemented()
    del ll
    return ""
