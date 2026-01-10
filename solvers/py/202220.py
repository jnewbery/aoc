from utils import exit_not_implemented
from collections import deque

def part1(ll: list[str], args=None) -> str:
    del args

    values_list: deque[int] = deque([int(x) for x in ll])
    list_len = len(values_list)
    index_list = deque(range(list_len))

    print(values_list)

    for i in range(list_len):
        index = index_list.index(i)
        val = values_list[index]
        # print(f"Moving {val} at index {index}")

        # rotate so that val is at the front
        values_list.rotate(-index)
        index_list.rotate(-index)
        # remove the element
        values_list.popleft()
        index_list.popleft()
        # rotate the deque
        values_list.rotate(-(val % list_len))
        index_list.rotate(-(val % list_len))
        values_list.appendleft(val)
        index_list.appendleft(index)
        # print(values_list)

    # print(values_list)

    zero_index = 0
    for n, x in enumerate(values_list):
        if x == 0:
            zero_index = n
    # breakpoint()
    i_1000 = values_list[(zero_index + 1000) % list_len]
    i_2000 = values_list[(zero_index + 2000) % list_len]
    i_3000 = values_list[(zero_index + 3000) % list_len]
    print(f"{i_1000=}, {i_2000=}, {i_3000=}")
    sol = i_1000 + i_2000 + i_3000
    return str(sol)

def part2(ll: list[str], args=None) -> str:
    del args
    exit_not_implemented()
    del ll
    return ""
