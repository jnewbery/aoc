def _extract_solution(coords: list[tuple[int, int]]) -> str:
    list_len = len(coords)

    i_0 = 0
    for n, x in enumerate(coords):
        if x[0] == 0:
            i_0 = n
    i_1000 = (i_0 + 1000) % list_len
    i_2000 = (i_0 + 2000) % list_len
    i_3000 = (i_0 + 3000) % list_len
    # print(f"{i_0=}, {i_1000=}, {i_2000=}, {i_3000=}")

    v_1000 = coords[(i_1000)][0]
    v_2000 = coords[(i_2000)][0]
    v_3000 = coords[(i_3000)][0]
    # print(f"{v_1000=}, {v_2000=}, {v_3000=}")

    sol = v_1000 + v_2000 + v_3000
    return str(sol)

def _shuffle_coords(coords: list[tuple[int, int]]) -> list[tuple[int, int]]:
    list_len = len(coords)

    # print("Initial arrangement:")
    # print(', '.join([str(coord[0]) for coord in coords]) + "\n")
    for i in range(len(coords)):
        for current_pos, p in enumerate(coords):
            val, orig_pos = p
            if orig_pos == i:
                new_pos = (current_pos + val) % (list_len - 1)
                # print(f"Moving {val} from position {current_pos} to position {new_pos}")

                coords.pop(current_pos)
                coords.insert(new_pos, p)
                # if new_pos > current_pos:
                #     coords.insert(new_pos, p)
                # else:
                #     coords.insert(new_pos, p)
                # print([p[1] for p in coords])
                break

    return coords

def part1(ll: list[str], args=None) -> str:
    del args

    # coords contains tuples of (value, original position)
    coords: list[tuple[int, int]] = [(int(x), n) for n, x in enumerate(ll)]
    # print(coords)

    coords = _shuffle_coords(coords)

    return _extract_solution(coords)

def part2(ll: list[str], args=None) -> str:
    del args
    # coords contains tuples of (value, original position)
    coords: list[tuple[int, int]] = [(int(x) * 811589153, n) for n, x in enumerate(ll)]
    # print(coords)

    for _ in range(10):
        coords = _shuffle_coords(coords)
        # print(coords)

    return _extract_solution(coords)
