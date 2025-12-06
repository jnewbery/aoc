from math import prod

def part1(ll: list[str]) -> str:
    operators = ll.pop(-1).split()
    rows = [[int(e) for e in l.split()] for l in ll]
    elements = zip(*rows)

    ret = 0
    for i, elements in enumerate(elements):
        if operators[i] == '+':
            ret += sum(elements)
            # print(operators[i], elements, sum(elements))
        else:
            ret += prod(elements)
            # print(operators[i], elements, prod(elements))

    return str(ret)

def part2(ll: list[str]) -> str:
    operator = None
    elements: list[int] = []
    ret = 0
    for i in range(len(ll[0])):
        col = ''.join([l[i] for l in ll])
        if col[-1] in ('+', '*'):
            operator = col[-1]
            elements = [int(col[:-1])]
        elif col.isspace():
            if operator == '+':
                ret += sum(elements)
                # print(operator, elements, sum(elements))
            else:
                ret += prod(elements)
                # print(operator, elements, prod(elements))
            operator = None
            elements = []
        else:
            elements.append(int(col))

    # Don't forget the last set of elements. It would be
    # tidier to merge this into the main loop.
    if operator == '+':
        ret += sum(elements)
        # print(operator, elements, sum(elements))
    else:
        ret += prod(elements)
        # print(operator, elements, prod(elements))

    return str(ret)
