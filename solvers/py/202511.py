from dataclasses import dataclass
from collections import defaultdict
from itertools import pairwise

@dataclass
class Device():
    name: str
    to_devices: list[str]
    depth: None | int  # greatest depth (longest path from start)

def get_devices(ll: list[str], start_name: str, end_name: str) -> dict[str, Device]:
    devices: dict[str, Device] = {}

    for l in ll:
        from_device, to_devices_str = l.split(": ")
        to_devices = to_devices_str.split()
        if start_name in to_devices:
            continue
        elif from_device == start_name:
            depth = 0
        else:
            depth = None
        devices[from_device] = Device(name=from_device, to_devices=to_devices, depth=depth)
    devices[end_name] = Device(name=end_name, to_devices=[], depth=None)
    return devices

def get_depths(devices: dict[str, Device], start_name: str) -> list[str]:
    depths: dict[str, int] = {start_name: 0}
    to_visit: list[str] = [start_name]
    while to_visit:
        visiting = devices[to_visit.pop()]
        assert visiting.name in depths
        for to_visit_str in visiting.to_devices:
            if to_visit_str not in depths or depths[to_visit_str] < depths[visiting.name] + 1:
                depths[to_visit_str] = depths[visiting.name] + 1
                to_visit.append(to_visit_str)

    return sorted(depths.keys(), key=lambda n: depths[n])

def get_paths(devices: dict[str, Device], devices_by_depth: list[str], start_name: str, end_name: str) -> int:
    assert start_name in devices_by_depth
    assert end_name in devices_by_depth
    assert devices_by_depth.index(start_name) < devices_by_depth.index(end_name)

    paths: defaultdict[str, int] = defaultdict(int)
    paths[start_name] = 1
    # breakpoint()
    for visiting_name in devices_by_depth[devices_by_depth.index(start_name):]:
        visiting = devices[visiting_name]
        if visiting_name == end_name:
            return paths[end_name]
        for to_visit_str in visiting.to_devices:
            paths[to_visit_str] += paths[visiting_name]

    # Shouldn't reach this point - we should always pass end_name as we iterate over devices_by_depth
    assert False

def part1(ll: list[str]) -> str:
    START_NAME = "you"
    END_NAME = "out"
    devices: dict[str, Device] = get_devices(ll, START_NAME, END_NAME)

    # calculate depths
    devices_by_depth = get_depths(devices, START_NAME)

    # BFS by depth
    paths = get_paths(devices, devices_by_depth, START_NAME, END_NAME)

    return str(paths)

def part2(ll: list[str]) -> str:
    START_NAME = "svr"
    END_NAME = "out"
    WAYPOINTS = ["fft", "dac"]

    devices: dict[str, Device] = get_devices(ll, START_NAME, END_NAME)

    # calculate depths
    devices_by_depth = get_depths(devices, START_NAME)

    sorted_waypoints = [START_NAME] + sorted(WAYPOINTS[:], key=lambda w: devices_by_depth.index(w) or 0) + [END_NAME]

    # BFS by depth to each waypoint in turn
    paths = 1
    for start, end in pairwise(sorted_waypoints):
        paths *= get_paths(devices, devices_by_depth, start, end)

    return str(paths)
