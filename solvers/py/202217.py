from itertools import count

_ROCKS_INPUT = [
   "####",

   ".#.\n"
   "###\n"
   ".#.",

   "..#\n"
   "..#\n"
   "###",

    "#\n"
    "#\n"
    "#\n"
    "#",

    "##\n"
    "##",
]

def _get_rocks() -> list[set[tuple[int, int]]]:
    rocks: list[set[tuple[int, int]]] = []
    for rock_input in _ROCKS_INPUT:
        rock: set[tuple[int, int]] = set()
        for y, rock_line in enumerate(reversed(rock_input.splitlines())):
            for x, rock_cell in enumerate(rock_line):
                if rock_cell == ".":
                    continue
                elif rock_cell == "#":
                    rock.add((x,y))
        rocks.append(rock)

    return rocks

def _move_rock(rock: set[tuple[int, int]], direction: tuple[int, int]) -> set[tuple[int, int]]:
    rock_out: set[tuple[int, int]] = set()
    for cell in rock:
        rock_out.add((cell[0] + direction[0], cell[1] + direction[1]))

    return rock_out

def _print_tunnel(rocks: set[tuple[int, int]], rock: set[tuple[int, int]]) -> None:
    top_height = max(y for _, y in rock)
    if rocks:
        top_height = max(max(y for _, y in rocks), top_height)
    for y in range(top_height, 0, -1):
        print("|", end="")
        for x in range(7):
            if (x, y) in rocks:
                print("#", end="")
            elif (x, y) in rock:
                print("@", end="")
            else:
                print(".", end="")
        print("|")
    print("+-------+\n")

def _solve(ll: list[str], num_rocks: int) -> str:
    max_height = 0
    stopped_rocks: set[tuple[int, int]] = set()
    winds: list[tuple[int, int]] = [(1, 0) if c == ">" else (-1, 0) for c in ll[0]]
    rocks = _get_rocks()

    # Cache of (rock_index, wind_index) -> (rock_count, max_height, last_cycle_len)
    cache: dict[tuple[int, int], tuple[int, int, int | None]] = {}
    rock_to_height: dict[int, int] = {}

    j = 0
    for i in count(1):
        rock = rocks[(i - 1) % len(rocks)]
        if i == num_rocks + 1:
            return str(max_height)
        rock = _move_rock(rock, (2, max_height + 4))

        while True:
            # Move rock according to wind direction
            next_wind = winds[j % len(winds)]
            j += 1
            next_rock_pos = _move_rock(rock, next_wind)
            if any((cell[0] < 0 or cell[0] >= 7 for cell in next_rock_pos)):
                pass
            elif any((cell in stopped_rocks for cell in next_rock_pos)):
                pass
            else:
                rock = next_rock_pos

            # Move rock down
            next_rock_pos = _move_rock(rock, (0, -1))
            if any((cell in stopped_rocks for cell in next_rock_pos)) or any((y == 1 for _, y in rock)):
                # Rock has landed
                break
            else:
                rock = next_rock_pos

        # Add rock cells to the stopped_rock set and update max_height
        stopped_rocks |= rock
        max_height = max(max_height, max((y for _, y in rock)))

        # Cycle detection
        rock_to_height[i] = max_height
        cache_key = (i % len(rocks), j % len(winds))
        if (cache_entry := cache.get(cache_key, None)) is not None:
            rock_diff = i - cache_entry[0]
            height_diff = max_height - cache_entry[1]
            # We can't stop at the first cycle, since the landing area may be different, and so subsequent
            # rocks will land differently. Only stop if there have been multiple cycles of the same length
            if cache_entry[2] == rock_diff:
                rocks_left = num_rocks - i
                cycles, remainder = divmod(rocks_left, rock_diff)
                # bit of a hairy calculation, but essentially:
                # - height up until now
                # - number of cycles left * height diff of a cycle
                # - height diff from this rock to the offset in the cycle of the remained
                height = max_height + cycles * height_diff + rock_to_height[cache_entry[0] + remainder] - rock_to_height[cache_entry[0]]
                return str(height)
            cache[cache_key] = (i, max_height, rock_diff)
        else:
            cache[cache_key] = (i, max_height, None)

    assert False, "Should always terminate"


def part1(ll: list[str], args=None) -> str:
    del args
    return _solve(ll, 2022)

def part2(ll: list[str], args=None) -> str:
    del args
    return _solve(ll, 1_000_000_000_000)
