from collections import deque
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def compress_coordinates(coordinates):
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


def flood_fill(borders, internal_point):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = set()
    queue = deque([internal_point])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        x, y = current
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in borders:
                queue.append((new_x, new_y))
    return visited


def create_borders(coordinates):
    borders = set()
    complete = coordinates + [coordinates[0]]
    for c1, c2 in zip(complete, complete[1:]):
        borders |= span(c1, c2)
    return borders


def calculate_area(rectangle):
    (x1, y1), (x2, y2) = rectangle
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def rectangle_inside(p1, p2, polygon):
    x1, y1 = p1
    x2, y2 = p2
    x_min, x_max = sorted((x1, x2))
    y_min, y_max = sorted((y1, y2))
    for x in range(x_min, x_max + 1):
        if (x, y_min) not in polygon or (x, y_max) not in polygon:
            return False
    for y in range(y_min, y_max + 1):
        if (x_min, y) not in polygon or (x_max, y) not in polygon:
            return False
    return True

def visualize_compressed_grid(compressed, borders, interior, output_path: Path) -> None:
    points = set(compressed) | borders | interior
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    grid = np.zeros((max_y + 1, max_x + 1), dtype=np.uint8)
    for x, y in interior:
        grid[y, x] = 1
    for x, y in borders:
        grid[y, x] = 2
    for x, y in compressed:
        grid[y, x] = 3

    cmap = ListedColormap(["#f8f9fa", "#d0ebff", "#102a43", "#e67700"])
    fig, ax = plt.subplots(figsize=(max(8, max_x / 6), max(6, max_y / 6)))
    im = ax.imshow(grid, origin="lower", cmap=cmap, interpolation="nearest")

    x_tick_step = max(1, (max_x + 1) // 20)
    y_tick_step = max(1, (max_y + 1) // 20)
    ax.set_xticks(range(0, max_x + 1, x_tick_step))
    ax.set_yticks(range(0, max_y + 1, y_tick_step))
    ax.set_xlabel("compressed x")
    ax.set_ylabel("compressed y")
    ax.set_title("2025-09 compressed grid")
    ax.grid(color="#adb5bd", linestyle="--", linewidth=0.4)

    cbar = fig.colorbar(im, ax=ax, ticks=[0.5, 1.5, 2.5, 3.5])
    cbar.ax.set_yticklabels(["empty", "interior", "border", "corner"])

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

def part2(ll: list[str], args=None) -> str:
    coordinates = [[int(num) for num in l.split(",")] for l in ll]
    interior_seed = (150, 150)
    compressed = compress_coordinates(coordinates)
    borders = create_borders(compressed)
    interior = flood_fill(borders, interior_seed)
    polygon = borders | interior

    if bool(getattr(args, "visualize", False)):
        output_path = Path(__file__).parent / "plots" / "202509b_compressed.png"
        visualize_compressed_grid(compressed, borders, interior, output_path)

    max_area = 0
    for i, p1 in enumerate(compressed):
        for j, p2 in enumerate(compressed):
            if j <= i:
                continue
            area = calculate_area((coordinates[i], coordinates[j]))
            if area <= max_area:
                continue
            if rectangle_inside(p1, p2, polygon):
                max_area = area

    return str(max_area)
