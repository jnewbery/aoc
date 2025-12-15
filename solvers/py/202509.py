from collections import deque
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def compress_coordinates(coordinates: list[tuple[int, int]]) -> list[tuple[int, int]]:
    x_values = [c[0] for c in coordinates]
    y_values = [c[1] for c in coordinates]
    unique_x, unique_y = sorted(set(x_values)), sorted(set(y_values))
    x_rank = {x: i for i, x in enumerate(unique_x)}
    y_rank = {y: i for i, y in enumerate(unique_y)}
    return [(x_rank[x], y_rank[y]) for x, y in coordinates]


def span(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    x_min, x_max = sorted((x1, x2))
    y_min, y_max = sorted((y1, y2))
    return {(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)}


def flood_fill(borders: set[tuple[int, int]],
               start_points: list[tuple[int, int]],
               x_max: int,
               y_max: int) -> set[tuple[int, int]]:
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = set()
    queue = deque(start_points)
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        x, y = current
        if x < 0 or y < 0 or x > x_max or y > y_max or (x, y) in borders:
            continue
        visited.add(current)
        for dx, dy in directions:
            queue.append((x + dx, y + dy))
    return visited


def create_borders(coordinates: list[tuple[int, int]]) -> set[tuple[int, int]]:
    borders = set()
    complete = coordinates + [coordinates[0]]
    for c1, c2 in zip(complete, complete[1:]):
        borders |= span(c1, c2)
    return borders


def calculate_area(rectangle: tuple[tuple[int, int], tuple[int, int]]) -> int:
    (x1, y1), (x2, y2) = rectangle
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def rectangle_overlaps(p1: tuple[int, int], p2: tuple[int, int], space: set[tuple[int, int]]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x_min, x_max = sorted((x1, x2))
    y_min, y_max = sorted((y1, y2))
    for x in range(x_min, x_max + 1):
        if (x, y_min) in space or (x, y_max) in space:
            return True
    for y in range(y_min, y_max + 1):
        if (x_min, y) in space or (x_max, y) in space:
            return True
    return False

def visualize_compressed_grid(compressed: list[tuple[int, int]],
                              borders: set[tuple[int, int]],
                              outside: set[tuple[int, int]],
                              output_path: Path) -> None:
    points = set(compressed) | borders | outside
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    grid = np.zeros((max_y + 1, max_x + 1), dtype=np.uint8)
    for x, y in outside:
        grid[y, x] = 1
    for x, y in borders:
        grid[y, x] = 2
    for x, y in compressed:
        grid[y, x] = 3

    cmap = ListedColormap(["#f8f9fa", "#d0ebff", "#102a43", "#e67700"])
    fig, ax = plt.subplots(figsize=(max(8, max_x / 6), max(6, max_y / 6)))
    ax.imshow(grid, origin="lower", cmap=cmap, interpolation="nearest")

    x_tick_step = max(1, (max_x + 1) // 20)
    y_tick_step = max(1, (max_y + 1) // 20)
    ax.set_xticks(range(0, max_x + 1, x_tick_step))
    ax.set_yticks(range(0, max_y + 1, y_tick_step))
    ax.grid(color="#adb5bd", linestyle="--", linewidth=0.4)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(output_path, dpi=220)
    plt.close(fig)

def part1(ll: list[str]) -> str:
    corners = []
    for l in ll:
        corners.append([int(c) for c in l.split(',')])

    largest = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
            largest = max(area, largest)

    return str(largest)

def part2(ll: list[str], args=None, visualize: bool = False) -> str:
    coordinates: list[tuple[int, int]] = []
    for l in ll:
        coord_str = l.split(",")
        coordinates.append((int(coord_str[0]), int(coord_str[1])))
    compressed = compress_coordinates(coordinates)
    borders = create_borders(compressed)

    max_x = max(x for x, _ in compressed)
    max_y = max(y for _, y in compressed)
    x_bound, y_bound = max_x + 1, max_y + 1

    outside_seeds = [(0, 0), (0, y_bound), (x_bound, 0), (x_bound, y_bound)]
    outside = flood_fill(borders, outside_seeds, x_bound, y_bound)

    if bool(getattr(args, "visualize", visualize)):
        output_path = Path(__file__).parent / "plots" / "202509_compressed.png"
        visualize_compressed_grid(compressed, borders, outside, output_path)

    max_area = 0
    for i in range(len(compressed)):
        for j in range(i + 1, len(compressed)):
            p1 = compressed[i]
            p2 = compressed[j]
            area = calculate_area((coordinates[i], coordinates[j]))
            if area <= max_area:
                continue
            if not rectangle_overlaps(p1, p2, outside):
                max_area = area

    return str(max_area)
