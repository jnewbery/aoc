from utils import exit_not_implemented

def part1(ll: list[str], args=None) -> str:
    del args

    original_list = [int(x) for x in ll]
    list_len = len(original_list)

    new_list = original_list.copy()
    # print(new_list)

    for i in original_list:
        i_index = new_list.index(i)
        new_list.pop(i_index)
        new_index = i_index + i
        if new_index <= 0:
            new_index += (list_len - 1)
        if new_index >= list_len:
            new_index -= (list_len - 1)
        # print(f"Moving {i} from {i_index} to {new_index}")
        new_list.insert(new_index, i)
        # print(new_list)

    print(new_list)

    zero_index = new_list.index(0)
    i_1000 = new_list[(zero_index + 1000) % list_len]
    print(f"{i_1000=}")
    i_2000 = new_list[(zero_index + 2000) % list_len]
    print(f"{i_2000=}")
    i_3000 = new_list[(zero_index + 3000) % list_len]
    print(f"{i_3000=}")
    sol = i_1000 + i_2000 + i_3000
    return str(sol)

def part2(ll: list[str], args=None) -> str:
    del args
    exit_not_implemented()
    del ll
    return ""
