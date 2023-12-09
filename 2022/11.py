#!/usr/bin/env python3
from functools import reduce
import operator

class Monkey:
    def __init__(self, items, operation, test_divisor, true_to, false_to):
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.true_to = true_to
        self.false_to = false_to
        self.inspections = 0
        # print(self)

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test_divisor}, {self.true_to}, {self.false_to}"


def get_monkeys(ll):
    monkeys = []
    while ll:
        ll.pop(0)  # Monkey index
        items = [int(i) for i in ll.pop(0).split(": ")[1].split(',')]
        operation = ll.pop(0).split(": new = ")[1]
        test_divisor = int(ll.pop(0).split(": divisible by ")[1])
        true_to = int(ll.pop(0).split(": throw to monkey ")[1])
        false_to = int(ll.pop(0).split(": throw to monkey ")[1])
        if ll:
            ll.pop(0)  # blank line
        monkeys.append(Monkey(items, operation, test_divisor, true_to, false_to))

    return monkeys

def monkey_round(monkeys, worry_operation):
    for i, monkey in enumerate(monkeys):
        # print(f"monkey {i}, items: {monkey.items}")
        while monkey.items:
            monkey.inspections += 1
            old = monkey.items.pop(0)  # noqa: F841 (`old` is used in the eval)
            # print(old)
            # print(monkey.operation)
            new = int(eval(monkey.operation))
            # print(new)
            new = worry_operation(new)
            # print(new)
            to_monkey = monkey.true_to if (new % monkey.test_divisor) == 0 else monkey.false_to
            # print(to_monkey)
            monkeys[to_monkey].items.append(new)

    # for monkey in monkeys:
    #     print(monkey)

def part1(ll):
    monkeys = get_monkeys(ll)
    for _ in range(20):
        monkey_round(monkeys, lambda x: x // 3)

    inspections = sorted([m.inspections for m in monkeys])
    # print(inspections)

    return inspections[-2] * inspections[-1]

def part2(ll):
    monkeys = get_monkeys(ll)
    divisor = reduce(operator.mul, [monkey.test_divisor for monkey in monkeys], 1)
    for _ in range(10000):
        monkey_round(monkeys, lambda x: x % divisor)

    inspections = sorted([m.inspections for m in monkeys])
    # print(inspections)

    return inspections[-2] * inspections[-1]
    raise NotImplementedError

TEST_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

TEST_SOL = [10605, 2713310158]

FULL_INPUT = """Monkey 0:
  Starting items: 65, 78
  Operation: new = old * 3
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 78, 86, 79, 73, 64, 85, 88
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 2:
  Starting items: 69, 97, 77, 88, 87
  Operation: new = old + 2
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 3:
  Starting items: 99
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 5

Monkey 4:
  Starting items: 60, 57, 52
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 5:
  Starting items: 91, 82, 85, 73, 84, 53
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 6:
  Starting items: 88, 74, 68, 56
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 7:
  Starting items: 54, 82, 72, 71, 53, 99, 67
  Operation: new = old + 1
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 0"""

FULL_SOL = [110264, 23612457316]
