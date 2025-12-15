from collections import deque

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

def part2(ll: list[str]) -> str:
    coordinates = [[int(num) for num in l.split(",")] for l in ll]
    interior_seed = (150, 150)
    compressed = compress_coordinates(coordinates)
    borders = create_borders(compressed)
    interior = flood_fill(borders, interior_seed)
    polygon = borders | interior
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
