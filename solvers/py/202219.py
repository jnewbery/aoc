from utils import exit_not_implemented, get_numbers
import numpy as np
import enum

# Vector is (ore_robots, ore, clay_robots, clay, obs_robot, obs, geode_robot, geode)
# Always start with 1 ord producing robot and nothing else
_STARTING_VECTOR: np.typing.NDArray = np.array([1, 0, 0, 0, 0, 0, 0, 0])
_MINING_MATRIX = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0],  # Ore robots stay the same
    [1, 1, 0, 0, 0, 0, 0, 0],  # Ore = previous ore + ore robots
    [0, 0, 1, 0, 0, 0, 0, 0],  # Clay robots stay the same
    [0, 0, 1, 1, 0, 0, 0, 0],  # Clay = previous clay + clay robots
    [0, 0, 0, 0, 1, 0, 0, 0],  # Obsidian robots stay the same
    [0, 0, 0, 0, 1, 1, 0, 0],  # Obsidian = previous obsidian + obsidian robots
    [0, 0, 0, 0, 0, 0, 1, 0],  # Geode robots stay the same
    [0, 0, 0, 0, 0, 0, 1, 1]   # Geode = previous geode + geode robots
    ])
# _MINUTES = 24
_MINUTES = 20

class _ACTIONS(enum.Enum):
    NONE = enum.auto()
    ORE = enum.auto()
    CLAY = enum.auto()
    OBS = enum.auto()
    GEODE = enum.auto()

def _make_robot_building_vector(robot_index: int, costs: tuple[int, int, int, int]) -> np.typing.NDArray:
    v = [0, 0, 0, 0, 0, 0, 0, 0]
    v[robot_index * 2] = 1  # add a robot
    for i, cost in enumerate(costs):
        v[(i * 2) + 1] = -cost

    return np.array(v)

def _best_result(action: _ACTIONS, minutes_left: int, v: np.typing.NDArray, actions: dict[_ACTIONS, np.typing.NDArray], max_costs: tuple[int, int, int]) -> int:
    if minutes_left == 0:
        return v[7]

    forbidden_acts: set[_ACTIONS] = set()
    if action == _ACTIONS.NONE:
        # See what actions were possible. We want to be greedy, so don't follow
        # a no-op with an action that we could have done earlier
        for act_name, act_vector in actions.items():
            if act_name == _ACTIONS.NONE:
                continue
            if np.min(v + act_vector) >= 0:
                # Can afford to make this robot
                forbidden_acts.add(act_name)

    # Allow bots to mine and carry out action
    new_v = _MINING_MATRIX @ v + actions[action]

    if np.min(new_v + actions[_ACTIONS.GEODE]) >= 0:
        # If you can build a geode bot, do it!
        return _best_result(_ACTIONS.GEODE, minutes_left - 1, new_v, actions, max_costs)

    max_ore_cost, max_clay_cost, max_obs_cost = max_costs
    best_result: int = _best_result(_ACTIONS.NONE, minutes_left - 1, new_v, actions, max_costs)  # Do nothing action
    if (new_v[0] < max_ore_cost) and (_ACTIONS.ORE not in forbidden_acts):
        # consider building an ore robot
        best_result = max(best_result, _best_result(_ACTIONS.ORE, minutes_left - 1, new_v, actions, max_costs))
    if new_v[2] < max_clay_cost and (_ACTIONS.CLAY not in forbidden_acts):
        # consider building a clay robot
        best_result = max(best_result, _best_result(_ACTIONS.CLAY, minutes_left - 1, new_v, actions, max_costs))
    if new_v[4] < max_obs_cost and (_ACTIONS.OBS not in forbidden_acts):
        # consider building an obsidian robot
        best_result = max(best_result, _best_result(_ACTIONS.OBS, minutes_left - 1, new_v, actions, max_costs))

    return best_result


def get_blueprint_quality(l: str) -> int:
    """Get the best number of geodes possible from a blueprint"""
    # print("Getting blueprint quality")
    params = get_numbers(l)
    blueprint_index = params.pop(0)
    # print(params)
    max_ore_cost = max(params[0], params[1], params[2], params[4])
    max_clay_cost = params[3]
    max_obs_cost = params[5]

    actions: dict[_ACTIONS, np.typing.NDArray] = {}
    actions[_ACTIONS.NONE] = np.array([0, 0, 0, 0, 0, 0, 0, 0])  # No-build
    actions[_ACTIONS.ORE] = _make_robot_building_vector(0, (params[0], 0, 0, 0))  # Ore robot
    actions[_ACTIONS.CLAY] = _make_robot_building_vector(1, (params[1], 0, 0, 0))  # Clay robot
    actions[_ACTIONS.OBS] = _make_robot_building_vector(2, (params[2], params[3], 0, 0))  # Obsidian robot
    actions[_ACTIONS.GEODE] = _make_robot_building_vector(3, (params[4], 0, params[5], 0))  # Geode robot
    # print(building_vectors)

    # best: list[np.typing.NDArray] = [_STARTING_VECTOR]
    # for minute in range(_MINUTES):
    #     new_best: list[np.typing.NDArray] = []
    #     for v in best:
    #         if np.min(v + actions[_ACTIONS.GEODE]) >= 0:
    #             # If you can build a geode bot, do it!
    #             new_best.append(_MINING_MATRIX @ v + actions[_ACTIONS.GEODE])
    #         else:
    #             for act_name, act_vector in actions.items():
    #                 if v[0] >= max_ore_cost and act_name == _ACTIONS.ORE:
    #                     # Don't need any more ore robots
    #                     continue
    #                 if v[2] >= max_clay_cost and act_name == _ACTIONS.CLAY:
    #                     # Don't need any more clay robots
    #                     continue
    #                 if v[4] >= max_obs_cost and act_name == _ACTIONS.OBS:
    #                     # Don't need any more obs robots
    #                     continue
    #                 if np.min(v + act_vector) < 0:
    #                     # Can't afford to make this robot
    #                     continue
    #                 else:
    #                     new_best.append(_MINING_MATRIX @ v + act_vector)
    #     best = new_best
    #     print(minute)
    #     print(f"{len(best)} candidates")

    #     # Remove a vector if a different vector has componentwise dominance
    #     # best.sort(key=lambda x: x.sum(), reverse=True)
    #     # # print(best)
    #     # i = 0
    #     # while len(best) > i:
    #     #     j = i + 1
    #     #     while len(best) > j:
    #     #         if np.all(best[i] >= best[j]):
    #     #             best.pop(j)
    #     #         else:
    #     #             j += 1
    #     #     i += 1
    #     # print(f"{len(best)} candidates after pruning")

    #     seen = set()
    #     out = []
    #     for a in best:
    #         a = np.asarray(a)
    #         key = (a.shape, a.dtype.str, a.tobytes())
    #         if key not in seen:
    #             seen.add(key)
    #             out.append(a)
    #     best = out

    return _best_result(_ACTIONS.NONE, _MINUTES, _STARTING_VECTOR, actions, (max_ore_cost, max_clay_cost, max_obs_cost))

    # return max(g for _, _, _, _, _, _, _, g in best) * blueprint_index

def part1(ll: list[str], args=None) -> str:
    del args
    quality = 0
    for l in ll:
        quality += get_blueprint_quality(l)
    return str(quality)

def part2(ll: list[str], args=None) -> str:
    del args
    exit_not_implemented()
    del ll
    return ""
