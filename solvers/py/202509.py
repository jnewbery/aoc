from typing import Self
import enum
import itertools
from dataclasses import dataclass
import heapq

@dataclass
class Coord():
    x: int
    y: int

    # Element-wise addition
    def __add__(self, other: Self) -> Self:
        return Coord(self.x + other.x, self.y + other.y)

    def __lt__(self, other: Self) -> bool:
        return self.x < other.x or self.y < other.y

    def direction(self, other: Self) -> "Direction":
        if self.x == other.x:
            if self.y < other.y:
                return Direction.UP
            elif self.y > other.y:
                return Direction.DOWN
            else:
                return Direction.SAME
        elif self.y == other.y:
            if self.x < other.x:
                return Direction.RIGHT
            else:  # self.x < other.x:
                return Direction.LEFT
        else:
            return Direction.OTHER

class Orientation(enum.Enum):
    VERTICAL = enum.auto()
    HORIZONTAL = enum.auto()
    OTHER = enum.auto()
    SAME = enum.auto()

@dataclass
class Line():
    from_coord: Coord
    to_coord: Coord

    @property
    def min_x(self) -> int:
        return min(self.from_coord.x, self.to_coord.x)

    @property
    def max_x(self) -> int:
        return max(self.from_coord.x, self.to_coord.x)

    @property
    def min_y(self) -> int:
        return min(self.from_coord.y, self.to_coord.y)

    @property
    def max_y(self) -> int:
        return max(self.from_coord.y, self.to_coord.y)

    @property
    def orientation(self) -> Orientation:
        match (self.from_coord.x == self.to_coord.x, self.from_coord.y == self.to_coord.y):
            case (True, True):
                return Orientation.SAME
            case (True, False):
                return Orientation.VERTICAL
            case (False, True):
                return Orientation.HORIZONTAL
            case _:
                return Orientation.OTHER

    def crossing(self, other: Self) -> bool:
        if self.orientation == Orientation.HORIZONTAL:
            if other.orientation == Orientation.HORIZONTAL:
                # both horizontal
                return self.min_y == other.min_y and other.min_x <= self.max_x and self.min_x <= other.max_x
            # self horizontal, other vertical
            return (self.min_x <= other.min_x <= self.max_x) and (other.min_y <= self.min_y <= other.max_y)
        # both vertical
        if other.orientation == Orientation.VERTICAL:
            return self.min_x == other.min_x and other.min_y <= self.max_y and self.min_y <= other.max_y
        # self vertical, other horizontal
        return (self.min_y <= other.min_y <= self.max_y) and (other.min_x <= self.min_x <= other.max_x)

class Direction(enum.Enum):
    UP = Coord(0, 1)
    DOWN = Coord(0, -1)
    LEFT = Coord(-1, 0)
    RIGHT = Coord(1, 0)
    SAME = Coord(0, 0)
    OTHER = None

def part1(ll: list[str]) -> str:
    corners = []
    for l in ll:
        corners.append([int(c) for c in l.split(',')])

    largest = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
            # print(i, corners[i], j, corners[j], area)
            largest = max(area, largest)

    return str(largest)

def part2(ll: list[str]) -> str:
    corners: list[Coord] = []
    for l in ll:
        corners.append(Coord(*[int(c) for c in l.split(',')]))
    # print(f"{corners=}")

    # corners of the shape that surrounds our shape (ie the first
    # row of tiles outside the shape
    outer_corners: list[Coord] = []

    for i in range(len(corners)):
        corner = corners[i]
        prev_corner = corners[(i - 1) % len(corners)]
        next_corner = corners[(i + 1) % len(corners)]
        # print(prev_corner, corner, next_corner)
        prev_direction = corner.direction(prev_corner)
        next_direction = corner.direction(next_corner)
        # print(prev_direction, next_direction)
        match (prev_direction, next_direction):
            case (Direction.LEFT, Direction.UP):
                outer_corners.append(corner + Direction.DOWN.value + Direction.RIGHT.value)
            case (Direction.LEFT, Direction.DOWN):
                outer_corners.append(corner + Direction.DOWN.value + Direction.LEFT.value)
            case (Direction.DOWN, Direction.LEFT):
                outer_corners.append(corner + Direction.UP.value + Direction.RIGHT.value)
            case (Direction.DOWN, Direction.RIGHT):
                outer_corners.append(corner + Direction.DOWN.value + Direction.RIGHT.value)
            case (Direction.RIGHT, Direction.UP):
                outer_corners.append(corner + Direction.UP.value + Direction.RIGHT.value)
            case (Direction.RIGHT, Direction.DOWN):
                outer_corners.append(corner + Direction.UP.value + Direction.LEFT.value)
            case (Direction.UP, Direction.LEFT):
                outer_corners.append(corner + Direction.UP.value + Direction.LEFT.value)
            case (Direction.UP, Direction.RIGHT):
                outer_corners.append(corner + Direction.DOWN.value + Direction.LEFT.value)
            case _:
                assert False

    #There are ~500 of these. It'd be better to index them efficiently so that we don't need
    # to iterate over all of them for each of the (500 * 499) / 2 possible squares.
    surrounding_lines = [Line(*p) for p in itertools.pairwise(outer_corners + [outer_corners[0]])]
    # print(f"{surrounding_lines=}")

    squares: list[tuple[int, tuple[Coord, Coord]]] = []
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            area = (abs(corners[i].x - corners[j].x) + 1) * (abs(corners[i].y - corners[j].y) + 1)
            squares.append((area, (corners[i], corners[j])))

    heapq.heapify_max(squares)
    while squares:
        square = heapq.heappop_max(squares)
        # print(square)
        corner1 = square[1][0]
        corner3 = square[1][1]
        corner2 = Coord(corner1.x, corner3.y)
        corner4 = Coord(corner3.x, corner1.y)
        edges = [Line(*p) for p in itertools.pairwise([corner1, corner2, corner3, corner4, corner1])]
        # print(edges)

        # for e in edges:
        #     for sl in surrounding_lines:
        #         print(f"Checking {e=} {sl=}")
        #         if e.crossing(sl):
        #             print(f"Crossing: {e} {sl}")
        if any([e.crossing(sl) for e in edges for sl in surrounding_lines]):
            # print(f"Crossing: {e} {sl}")
            # print("crossing")
            continue
        else:
            # print("No crossing!")
            return str(square[0])

    return ""
