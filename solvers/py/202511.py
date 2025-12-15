from collections import defaultdict
from itertools import pairwise

def get_devices(ll: list[str], start_name: str, end_name: str) -> dict[str, list[str]]:
    devices: dict[str, list[str]] = {}

    for l in ll:
        from_device, to_devices_str = l.split(": ")
        to_devices = to_devices_str.split()
        if start_name in to_devices:
            continue
        devices[from_device] = to_devices
    devices[end_name] = []
    return devices

def get_devices_depth_order(devices: dict[str, list[str]], start_name: str) -> list[str]:
    depths: dict[str, int] = {start_name: 0}
    to_visit: list[str] = [start_name]
    while to_visit:
        visiting_str = to_visit.pop()
        visiting_next = devices[visiting_str]
        assert visiting_str in depths
        for to_visit_str in visiting_next:
            if to_visit_str not in depths or depths[to_visit_str] < depths[visiting_str] + 1:
                depths[to_visit_str] = depths[visiting_str] + 1
                to_visit.append(to_visit_str)

    return sorted(depths.keys(), key=lambda n: depths[n])

def get_paths(devices: dict[str, list[str]], devices_depth_order: list[str], start_name: str, end_name: str) -> int:
    assert start_name in devices_depth_order
    assert end_name in devices_depth_order
    assert devices_depth_order.index(start_name) < devices_depth_order.index(end_name)

    paths: defaultdict[str, int] = defaultdict(int)
    paths[start_name] = 1
    for visiting_name in devices_depth_order[devices_depth_order.index(start_name):]:
        visiting_next = devices[visiting_name]
        if visiting_name == end_name:
            return paths[end_name]
        for to_visit_str in visiting_next:
            paths[to_visit_str] += paths[visiting_name]

    # Shouldn't reach this point - we should always pass end_name as we iterate over devices_depth_order
    assert False

def part1(ll: list[str]) -> str:
    START_NAME = "you"
    END_NAME = "out"
    devices: dict[str, list[str]] = get_devices(ll, START_NAME, END_NAME)

    # Calculate depth order
    devices_depth_order = get_devices_depth_order(devices, START_NAME)

    # BFS by depth
    paths = get_paths(devices, devices_depth_order, START_NAME, END_NAME)

    return str(paths)

def part2(ll: list[str]) -> str:
    START_NAME = "svr"
    END_NAME = "out"
    WAYPOINTS = ["fft", "dac"]

    devices: dict[str, list[str]] = get_devices(ll, START_NAME, END_NAME)

    # Calculate depth order
    devices_depth_order = get_devices_depth_order(devices, START_NAME)

    sorted_waypoints = [START_NAME] + sorted(WAYPOINTS[:], key=lambda w: devices_depth_order.index(w) or 0) + [END_NAME]

    # BFS by depth to each waypoint in turn
    paths = 1
    for start, end in pairwise(sorted_waypoints):
        paths *= get_paths(devices, devices_depth_order, start, end)

    return str(paths)
