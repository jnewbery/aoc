from utils import exit_not_implemented

def _extract_solution(coords: list[tuple[int, bool]]) -> str:
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

def _shuffle_coords(coords: list[tuple[int, bool]]) -> list[tuple[int, bool]]:
    list_len = len(coords)

    for _ in range(len(coords)):
        # Moving items in the list is commutative, so we don't need to move them in
        # order of the original list. We can just scan through the list and move
        # the first item we find that still needs to be moved.
        for current_pos, p in enumerate(coords):
            val, to_move = p
            if to_move:
                new_pos = (current_pos + val) % (list_len - 1)
                # print(f"Moving {val} from position {current_pos} to position {new_pos}")

                if new_pos > current_pos:
                    coords = coords[:current_pos] + coords[current_pos + 1:new_pos + 1] + [p] + coords[new_pos + 1:]
                elif new_pos < current_pos:
                    coords = coords[:new_pos] + [p] + coords[new_pos:current_pos] + coords[current_pos + 1:]
                coords[new_pos] = (coords[new_pos][0], False)
                # print([p[1] for p in coords])
                break
    return coords

def part1(ll: list[str], args=None) -> str:
    del args

    # coords contains tuples of (value, has moved)
    # TODO: reimplement this as a deque. To re-order, rotate the deque so that the
    #       element to move is at the front, pop it, rotate the deque by the corrent number
    #       and then push the element to the front. Now that I have a correct solution,
    #       I can print a trace of what the co-ords look like after every move to verify
    #       the new deque soluton.
    coords: list[tuple[int, bool]] = [(int(x), True) for x in ll]
    # print(coords)

    coords = _shuffle_coords(coords)

    return _extract_solution(coords)

def part2(ll: list[str], args=None) -> str:
    del args
    exit_not_implemented()
    del ll
    return ""
