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

@dataclass
class Monkey2():
    left: str | int | None = None
    right: str | int | None = None
    num: int | None = None
    operation: Callable | None = None

    def __init__(self, name: str, l: str):
        parts = l.split()
        if name == "root":
            self.operation = operator.sub
            self.num = 0
            self.left = parts[0]
            self.right = parts[2]
            return
        if name == "humn":
            self.operation = None
            self.left = None
            self.right = None
            self.num = None
            return
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

    def val(self, monkeys: dict[str, Monkey2]) -> int | None:
        if self.num is not None:
            return self.num
        assert self.operation
        if type(self.left) == str:
            left = monkeys[self.left].val(monkeys)
            if left is not None:
                self.left = left
        if type(self.right) == str:
            right = monkeys[self.right].val(monkeys)
            if right is not None:
                self.right = right
        if type(self.left) == int and type(self.right) == int:
            self.num = self.operation(self.left, self.right)
            return self.num
        return None


def part2(ll: list[str], args=None) -> str:
    del args

    monkeys: dict[str, Monkey2] = {}
    for l in ll:
        name, monkey = l.split(": ")
        monkeys[name] = Monkey2(name, monkey)

    for k, v in monkeys.items():
        print(k, v)
    monkeys["root"].val(monkeys)
    print()
    for k, v in monkeys.items():
        print(k, v)
    return ""
