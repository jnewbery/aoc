from utils import exit_not_implemented
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict
from itertools import product
from typing import Generator

_DISTANCE = 30
_INF = 100  # May as well be infinity for distances in this graph

def _visualize_valves(valves: dict[str, int], tunnels: dict[str, dict[str, int]]) -> None:
    output_path = Path(__file__).parent / "plots" / "202216_valves.png"
    G = nx.Graph()
    for valve, flow_rate in valves.items():
        if valve == "AA":
            # Highlight starting valve
            color = "red"
        elif flow_rate > 0:
            # Highlight valves with positive flow rate
            color = "orange"
        else:
            color = "lightblue"
        G.add_node(valve, color=color)
        for to_valve, weight in tunnels[valve].items():
            G.add_edge(valve, to_valve, weight=weight)
    pos = nx.kamada_kawai_layout(G)

    plt.figure(figsize=(12, 8))
    node_colors = [G.nodes[n].get("color", "lightblue") for n in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=50, font_size=5, font_weight="bold", edge_color="gray")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=220)
    plt.close()

def _print_distances(distances: dict[str, dict[str, int]]) -> None:
    import numpy as np
    mat = np.array([[distances[i][j] for j in distances] for i in distances])
    np.set_printoptions(linewidth=200, suppress=True)
    print([i for i in distances.keys()])
    print(mat)

def _dfs(from_valve: str,
         path: list[tuple[str, int]],
         candidates: set[str],
         distance_left: int,
         distances: dict[str, dict[str, int]],
         weights: dict[str, int]) -> Generator[list[tuple[str, int]], None, None]:
    # print(from_valve, path, candidates, distance_left)
    reachable = {c for c in candidates if distances[from_valve][c] + 1 < distance_left and c != from_valve}
    if not reachable:
        yield path
        return
    for candidate in reachable:
        step_distance = distances[from_valve][candidate] + 1
        yield from _dfs(from_valve=candidate,
                        path=path + [(candidate, distance_left - step_distance)],
                        candidates=reachable,
                        distance_left=distance_left - step_distance,
                        distances=distances,
                        weights=weights)


def part1(ll: list[str], args=None) -> str:
    valves: dict[str, int] = {}
    tunnels: dict[str, dict[str, int]] = {}

    for l in ll:
        words = l.split()
        from_valve = words[1]
        flow = int(words[4].split("=")[1][:-1])
        to_valves = [w.strip(",") for w in words[9:]]
        valves[from_valve] = flow
        for to_valve in to_valves:
            if from_valve not in tunnels:
                tunnels[from_valve] = {}
            tunnels[from_valve][to_valve] = 1  # all tunnels have equal weight
    # print(f"Initial number of valves: {len(valves)}, edges: {sum(len(v) for v in tunnels.values()) // 2}")

    # If a valve has zero flow rate and only two neighbours, we can remove it
    # and connect its neighbors directly
    simplified = True
    while simplified:
        simplified = False
        for valve, flow_rate in list(valves.items()):
            if flow_rate == 0 and valve != "AA" and len(tunnels[valve]) == 2:
                neighbors = list(tunnels[valve].keys())
                total_distance = tunnels[neighbors[0]][valve] + tunnels[neighbors[1]][valve]
                del tunnels[neighbors[0]][valve]
                del tunnels[neighbors[1]][valve]
                tunnels[neighbors[0]][neighbors[1]] = total_distance
                tunnels[neighbors[1]][neighbors[0]] = total_distance
                del tunnels[valve]
                del valves[valve]
                simplified = True
                break
    # print(f"Simplified number of valves: {len(valves)}, edges: {sum(len(v) for v in tunnels.values()) // 2}")

    if bool(getattr(args, "visualize", False)):
        _visualize_valves(valves, tunnels)

    # Use Floyd–Warshall to find shortest paths between all pairs of valves
    # Initialize distances with neighbours
    distances: defaultdict[str, dict[str, int]] = defaultdict(dict)
    for from_valve, to_valve in product(valves.keys(), valves.keys()):
        if from_valve == to_valve:
            distances[from_valve][to_valve] = 0
        else:
            distances[from_valve][to_valve] = _INF  # may as well be infinite
    for from_valve, to_valves in tunnels.items():
        for to_valve, dist in to_valves.items():
            distances[from_valve][to_valve] = dist
    # _print_distances(distances)

    # Run the FW algorithm
    for k, i, j in product(valves.keys(), valves.keys(), valves.keys()):
        if distances[i][j] > distances[i][k] + distances[k][j]:
            distances[i][j] = distances[i][k] + distances[k][j]
    # _print_distances(distances)

    # DFS over the simplified graph to get all valid paths
    # TODO: pruning to avoid exploring bad branches
    candidate_valves = set(valves.keys())
    from_valve = "AA"
    candidate_valves -= {from_valve}
    max_score = 0
    for path in _dfs(from_valve, [(from_valve, _DISTANCE)], candidate_valves, _DISTANCE, distances, valves):
        # print(path, sum(valves[v] * t for v, t in path))
        max_score = max(max_score, sum(valves[v] * t for v, t in path))

    return(str(max_score))

def part2(ll: list[str], args=None) -> str:
    exit_not_implemented()
    del ll
    del args
    return ""
