from utils import exit_not_implemented

_ADJACENCIES = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

def part1(ll: list[str], args=None) -> str:
    del args
    cubes: list[tuple[int, int, int]] = []
    faces: set[tuple[int, int, int]] = set()
    for l in ll:
        # Scale up by 2x so that the spaces between cubes have integer coords
        coords = [int(d) * 2 for d in l.split(",")]
        cube = (coords[0], coords[1], coords[2])
        cubes.append(cube)
        for adjacency in _ADJACENCIES:
            face = (cube[0] + adjacency[0], cube[1] + adjacency[1], cube[2] + adjacency[2])
            faces ^= {face}
            
    return str(len(faces))

def part2(ll: list[str], args=None) -> str:
    exit_not_implemented()
    del ll
    del args
    return ""
