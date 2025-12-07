from functools import reduce, partial
import operator

class Monkey:
    def __init__(self, items, operation, test_divisor, true_to, false_to):
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.true_to = true_to
        self.false_to = false_to
        self.inspections = 0

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test_divisor}, {self.true_to}, {self.false_to}"


def get_monkeys(ll):
    monkeys = []
    while ll:
        ll.pop(0)  # Monkey index
        items = [int(i) for i in ll.pop(0).split(": ")[1].split(',')]
        operation_str = ll.pop(0).split(": new = ")[1]
        if operation_str == "old * old":
            operation = partial(pow, exp=2)
        elif operation_str[0:5] == 'old +':
            operation = partial(operator.add, int(operation_str[6:]))
        elif operation_str[0:5] == 'old *':
            operation = partial(operator.mul, int(operation_str[6:]))
        else:
            assert False, operation_str

        test_divisor = int(ll.pop(0).split(": divisible by ")[1])
        true_to = int(ll.pop(0).split(": throw to monkey ")[1])
        false_to = int(ll.pop(0).split(": throw to monkey ")[1])
        if ll:
            ll.pop(0)  # blank line
        monkeys.append(Monkey(items, operation, test_divisor, true_to, false_to))

    return monkeys

def monkey_round(monkeys, worry_operation):
    for monkey in monkeys:
        while monkey.items:
            monkey.inspections += 1
            old = monkey.items.pop(0)  # ignore
            new = monkey.operation(old)
            new = worry_operation(new)
            to_monkey = monkey.true_to if (new % monkey.test_divisor) == 0 else monkey.false_to
            monkeys[to_monkey].items.append(new)

def part1(ll: list[str]) -> str:
    monkeys = get_monkeys(ll)
    for _ in range(20):
        monkey_round(monkeys, lambda x: x // 3)

    inspections = sorted([m.inspections for m in monkeys])

    return inspections[-2] * inspections[-1]

def part2(ll: list[str]) -> str:
    monkeys = get_monkeys(ll)
    divisor = reduce(operator.mul, [monkey.test_divisor for monkey in monkeys], 1)
    for _ in range(10000):
        monkey_round(monkeys, lambda x: x % divisor)

    inspections = sorted([m.inspections for m in monkeys])

    return inspections[-2] * inspections[-1]
