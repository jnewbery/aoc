from dataclasses import dataclass
from utils import exit_not_implemented
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

@dataclass
class Valve:
    name: str
    flow_rate: int
    to_valves: list[str]

def visualize_valves(valves: dict[str, Valve], output_path: Path) -> None:
    G = nx.Graph()
    for valve in valves.values():
        if valve.name == "AA":
            # Highlight starting valve
            color = "red"
        elif valve.flow_rate > 0:
            # Highlight valves with positive flow rate
            color = "orange"
        else:
            color = "lightblue"
        G.add_node(valve.name, color=color)
        for to_valve in valve.to_valves:
            G.add_edge(valve.name, to_valve)
    pos = nx.kamada_kawai_layout(G)

    plt.figure(figsize=(12, 8))
    node_colors = [G.nodes[n].get("color", "lightblue") for n in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=50, font_size=5, font_weight="bold", edge_color="gray")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=220)
    plt.close()


def part1(ll: list[str], args=None) -> str:
    valves: dict[str, Valve] = {}
    for l in ll:
        words = l.split()
        from_valve = words[1]
        flow = int(words[4].split("=")[1][:-1])
        to_valves = [w.strip(",") for w in words[9:]]
        valves[from_valve] = Valve(from_valve, flow, to_valves)
    if bool(getattr(args, "visualize", False)):
        output_path = Path(__file__).parent / "plots" / "202216_valves.png"
        visualize_valves(valves, output_path)

    exit_not_implemented()
    assert False, "Not implemented"

def part2(ll: list[str], args=None) -> str:
    exit_not_implemented()
    del ll
    del args
    return ""
