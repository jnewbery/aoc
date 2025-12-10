import math

import numpy as np
from PIL import Image

def part1(ll: list[str]) -> str:
    corners = []
    for l in ll:
        corners.append([int(c) for c in l.split(',')])
    # print(corners)

    largest = 0
    for i in range(len(corners)):
        for j in range(i + 1, len(corners)):
            area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
            # print(i, corners[i], j, corners[j], area)
            largest = max(area, largest)

    return str(largest)

def part2(ll: list[str]) -> str:
    vertices = []
    for l in ll:
        vertices.append([int(c) for c in l.split(',')])

    xs = [c[0] for c in vertices]
    ys = [c[1] for c in vertices]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    target_max_dim = 2000  # keep the array at a manageable size
    span_x = max_x - min_x
    span_y = max_y - min_y
    scale = max(1, math.ceil(max(span_x, span_y) / target_max_dim))

    # Normalize to the scaled, zero-based grid and add a small padding
    normalized: list[tuple[int, int]] = [((x - min_x) // scale, (y - min_y) // scale) for x, y in vertices]
    padding = 2
    shifted: list[tuple[int, int]] = [(x + padding, y + padding) for x, y in normalized]

    width = max(x for x, _ in shifted) + padding + 1
    height = max(y for _, y in shifted) + padding + 1
    grid = np.zeros((height, width, 3), dtype=np.uint8)

    red = np.array([255, 0, 0], dtype=np.uint8)
    green = np.array([0, 255, 0], dtype=np.uint8)

    def draw_line(p0: tuple[int, int], p1: tuple[int, int]) -> None:
        """Bresenham line drawing directly into the numpy grid."""
        x0, y0 = p0
        x1, y1 = p1
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1 if x0 > x1 else 0
        sy = 1 if y0 < y1 else -1 if y0 > y1 else 0

        x, y = x0, y0
        grid[y, x] = green
        if dx == 0 and dy == 0:
            return

        if dx >= dy:
            err = dx // 2
            while x != x1:
                x += sx
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                grid[y, x] = green
        else:
            err = dy // 2
            while y != y1:
                y += sy
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                grid[y, x] = green

    # Draw edges between consecutive vertices and close the loop.
    for start, end in zip(shifted, shifted[1:] + [shifted[0]]):
        draw_line(start, end)

    # Highlight the vertices after drawing the lines so they stay red.
    for x, y in shifted:
        grid[y, x] = red

    image = Image.fromarray(grid, mode="RGB")
    image.show(title="202509 grid")

    return "shown"
