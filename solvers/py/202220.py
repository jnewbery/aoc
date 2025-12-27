from utils import exit_not_implemented
from collections import deque

def part1(ll: list[str], args=None) -> str:
    del args

    d: deque[tuple[int, int]] = deque([(n, int(x)) for n,x in enumerate(ll)])
    list_len = len(d)

    print(d)

    for i in range(len(d)):
        for current_pos, p in enumerate(d):
            if p[0] == i:
                print(f"Moving {p[1]}")

                # rotate so that i is at the front
                d.rotate(-current_pos)
                # remove the element
                d.popleft()
                # rotate the deque
                d.rotate(-(i + 1))
                d.appendleft(p)
                print([p[1] for p in d])
                break

    # print(d)

    zero_index = 0
    for n, x in enumerate(d):
        if x == 0:
            zero_index = n
    # breakpoint()
    i_1000 = d[(zero_index + 1000) % list_len][1]
    i_2000 = d[(zero_index + 2000) % list_len][1]
    i_3000 = d[(zero_index + 3000) % list_len][1]
    print(f"{i_1000=}, {i_2000=}, {i_3000=}")
    sol = i_1000 + i_2000 + i_3000
    return str(sol)

def part2(ll: list[str], args=None) -> str:
    del args
    exit_not_implemented()
    del ll
    return ""
