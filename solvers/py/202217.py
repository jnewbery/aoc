from utils import exit_not_implemented

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
    ret = []
    for rock_input in _ROCKS_INPUT:
        pass

    return ret


def part1(ll: list[str], args=None) -> str:
    del args
    max_height = 0
    stopped_rocks: set[tuple[int, int]] = set()
    winds: list[bool] = [True if c == ">" else False for c in ll[0]]

    exit_not_implemented()
    return ""

def part2(ll: list[str], args=None) -> str:
    exit_not_implemented()
    del ll
    del args
    return ""
