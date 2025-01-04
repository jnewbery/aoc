import functools

def get_pairs(ll):
    while ll:
        a = eval(ll.pop(0))
        b = eval(ll.pop(0))
        if ll:
            ll.pop(0)  # empty line
        yield a, b

def compare(a: list | int, b: list | int) -> int:
    # print(f"comparing {a} and {b}")
    if type(a) == int and type(b) == int:
        if a < b:
            return -1
        if a > b:
            return 1
        return 0
    
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            comp = compare(a[i], b[i])
            if comp != 0:
                return comp
        if len(a) < len(b):
            return -1
        if len(a) > len(b):
            return 1
        return 0
    
    if type(a) == list and type(b) == int:
        return compare(a, [b])

    # else type(b) == list and type(a) == int:
    return compare([a], b)

def part1(ll: list[str]) -> str:
    sol = 0
    for i, pair in enumerate(get_pairs(ll)):
        # print(i + 1, pair)
        if compare(pair[0], pair[1]) == -1:
            # print("in order")
            sol += i + 1
    return str(sol)

def part2(ll: list[str]) -> str:
    signals: list[list[list[int]]] = [eval(l) for l in ll if l]
    signals += [[[2]], [[6]]]
    signals.sort(key=functools.cmp_to_key(compare))
    return str((signals.index([[2]]) + 1) * (signals.index([[6]]) + 1))
