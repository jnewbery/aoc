from dataclasses import dataclass

@dataclass
class Device():
    name: str
    to_devices: list[str]
    depth: None | int  # greatest depth (longest path from start)
    paths: int # number of different paths to reach this device

def get_devices(ll: list[str], start_name: str, end_name: str) -> dict[str, Device]:
    devices: dict[str, Device] = {}

    for l in ll:
        from_device, to_devices_str = l.split(": ")
        to_devices = to_devices_str.split()
        if start_name in to_devices:
            continue
        elif from_device == start_name:
            depth = 0
            paths = 1
        else:
            depth = None
            paths = 0
        devices[from_device] = Device(name=from_device, to_devices=to_devices, depth=depth, paths=paths)
    devices[end_name] = Device(name=end_name, to_devices=[], depth=None, paths=0)
    return devices

def get_depths(devices: dict[str, Device], start_name: str, end_name: str) -> list[str]:
    to_visit: list[str] = [start_name]
    while to_visit:
        visiting = devices[to_visit.pop()]
        assert visiting.depth is not None
        for to_visit_str in visiting.to_devices:
            # if to_visit_str == end_name:
            #     continue
            to_visit_device = devices[to_visit_str]

            if to_visit_device.depth == None or to_visit_device.depth < visiting.depth + 1:
                to_visit_device.depth = visiting.depth + 1
                to_visit.append(to_visit_str)

    devices_by_depth: list[Device] = [d for d in devices.values() if d.depth is not None]
    devices_by_depth.sort(key=lambda d: d.depth or 0)

    return [d.name for d in devices_by_depth] + [end_name]

def get_paths(devices: dict[str, Device], devices_by_depth: list[str], end_name: str):
    for visiting_name in devices_by_depth:
        visiting = devices[visiting_name]
        if devices == end_name:
            return
        for to_visit_str in visiting.to_devices:
            devices[to_visit_str].paths += visiting.paths

def part1(ll: list[str]) -> str:
    START_NAME = "you"
    END_NAME = "out"
    devices: dict[str, Device] = get_devices(ll, START_NAME, END_NAME)

    # calculate depths
    devices_by_depth = get_depths(devices, START_NAME, END_NAME)

    # BFS by depth
    get_paths(devices, devices_by_depth, END_NAME)

    return str(devices[END_NAME].paths)

def part2(ll: list[str]) -> str:
    START_NAME = "svr"
    END_NAME = "out"
    WAYPOINTS = ["fft", "dac"]

    devices: dict[str, Device] = get_devices(ll, START_NAME, END_NAME)

    # calculate depths
    devices_by_depth = get_depths(devices, START_NAME, END_NAME)

    waypoints = WAYPOINTS[:]
    waypoints.sort(key=lambda w: devices[w].depth or 0)
    waypoints.append(END_NAME)

    # BFS by depth
    for waypoint in waypoints:
        get_paths(devices, devices_by_depth, waypoint)
        for d in devices.values():
            if d.name != waypoint:
                d.paths = 0
    # get_paths(devices, devices_by_depth, END_NAME)

    return str(devices[END_NAME].paths)
