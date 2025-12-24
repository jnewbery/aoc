from collections import deque

_ADJACENCIES = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

_DIRECTIONS = [(2 * x, 2 * y, 2 * z) for x, y, z in _ADJACENCIES]

def get_faces(cubes: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    faces: set[tuple[int, int, int]] = set()
    for cube in cubes:
        cube_x, cube_y, cube_z = cube
        for dx, dy, dz in _ADJACENCIES:
            face = (cube_x + dx, cube_y + dy, cube_z + dz)
            faces ^= {face}

    return faces

def part1(ll: list[str], args=None) -> str:
    del args
    cubes: set[tuple[int, int, int]] = set()
    for l in ll:
        # Scale up by 2x so that the spaces between cubes have integer coords
        coords = [int(d) * 2 for d in l.split(",")]
        cube = (coords[0], coords[1], coords[2])
        cubes.add(cube)
            
    return str(len(get_faces(cubes)))

def flood_fill(borders: set[tuple[int, int, int]],
               start_point: tuple[int, int, int],
               min_coords: tuple[int, int, int],
               max_coords: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    min_x, min_y, min_z = min_coords
    max_x, max_y, max_z = max_coords

    visited: set[tuple[int, int, int]] = set()
    queue = deque([start_point])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        x, y, z = current
        if x < min_x or y < min_y or z < min_z or x > max_x or y > max_y or z > max_z or (x, y, z) in borders:
            continue
        visited.add(current)
        for dx, dy, dz in _DIRECTIONS:
            queue.append((x + dx, y + dy, z + dz))
    return visited

def part2(ll: list[str], args=None) -> str:
    del args

    cubes: list[tuple[int, int, int]] = []
    for l in ll:
        # Scale up by 2x so that the spaces between cubes have integer coords
        coords = [int(d) * 2 for d in l.split(",")]
        cube = (coords[0], coords[1], coords[2])
        cubes.append(cube)

    # Expand space to +1 around lowest/highest values in each dimension
    min_coords = (-2, -2, -2)
    max_coords = (max(x for x, _, _ in cubes) + 2,
                  max(y for _, y, _ in cubes) + 2,
                  max(z for _, _, z in cubes) + 2)
    # print(f"({min_coords}) -> {max_coords}")

    # flood-fill entire outer space from (-2, -2, -2)
    outer_space = flood_fill(set(cubes), min_coords, min_coords, max_coords)
    # print(len(outer_space))

    # Calculate exposed faces of flood-filled inverse space
    faces = get_faces(outer_space)
    # print(len(faces))

    def is_in_space(coord: tuple[int, int, int]) -> bool:
        x, y, z = coord
        min_x, min_y, min_z = min_coords
        max_x, max_y, max_z = max_coords
        return min_x < x < max_x and min_y < y < max_y and min_z < z < max_z

    # Remove outer faces from outer_space faces
    inner_faces = sum(1 for face in faces if is_in_space(face))
    return str(inner_faces)
