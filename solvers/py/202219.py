from utils import get_numbers
import enum
from dataclasses import dataclass, replace
from itertools import islice

class Action(enum.Enum):
    NONE = enum.auto()
    ORE = enum.auto()
    CLAY = enum.auto()
    OBS = enum.auto()
    GEO = enum.auto()

@dataclass
class Inventory:
    ore_bots: int
    ore: int
    clay_bots: int
    clay: int
    obs_bots: int
    obs: int
    geo_bots: int
    geo: int

    @property
    def total(self) -> int:
        return self.ore_bots + self.ore + self.clay_bots + self.clay + self.obs_bots + self.obs + self.geo_bots + self.geo

    def dominates(self, other: Inventory) -> bool:
        return (self.ore_bots >= other.ore_bots and
            self.ore >= other.ore and
            self.clay_bots >= other.clay_bots and
            self.clay >= other.clay and
            self.obs_bots >= other.obs_bots and
            self.obs >= other.obs and
            self.geo_bots >= other.geo_bots and
            self.geo >= other.geo)

@dataclass
class InventoryWithForbiddenActions:
    inv: Inventory
    # Our algorithm *must* be greedy. If it's possible to build a bot
    # in one minute, but instead we do nothing, we can't build the same
    # bot the following minute.
    forbidden_actions: set[Action]

@dataclass
class Blueprint:
    ore_bot_ore_cost: int
    clay_bot_ore_cost: int
    obs_bot_ore_cost: int
    obs_bot_clay_cost: int
    geo_bot_ore_cost: int
    geo_bot_obs_cost: int

    @property
    def max_ore_cost(self) -> int:
        return max(self.ore_bot_ore_cost, self.clay_bot_ore_cost, self.obs_bot_ore_cost, self.geo_bot_ore_cost)

    @property
    def max_clay_cost(self) -> int:
        return self.obs_bot_clay_cost

    @property
    def max_obs_cost(self) -> int:
        return self.geo_bot_obs_cost

def _apply_action(inv: Inventory, blueprint: Blueprint, act: Action) -> Inventory:
    new_inv = replace(inv)
    new_inv.ore += new_inv.ore_bots
    new_inv.clay += new_inv.clay_bots
    new_inv.obs += new_inv.obs_bots
    new_inv.geo += new_inv.geo_bots
    match act:
        case Action.NONE:
            pass
        case Action.ORE:
            new_inv.ore_bots += 1
            new_inv.ore -= blueprint.ore_bot_ore_cost
        case Action.CLAY:
            new_inv.clay_bots += 1
            new_inv.ore -= blueprint.clay_bot_ore_cost
        case Action.OBS:
            new_inv.obs_bots += 1
            new_inv.ore -= blueprint.obs_bot_ore_cost
            new_inv.clay -= blueprint.obs_bot_clay_cost
        case Action.GEO:
            new_inv.geo_bots += 1
            new_inv.ore -= blueprint.geo_bot_ore_cost
            new_inv.obs -= blueprint.geo_bot_obs_cost
            pass
    return new_inv

def _possible_actions(inv: Inventory, blueprint: Blueprint) -> set[Action]:
    """Determine whether we can/should build a bot of any type. We check that:
        - we have enough resource to build that bot
        - and there are fewer bots of that resource type than the greatest cost for that resource
          type (otherwise there's no benefit to building another robot of that type
        """
    possible_actions: set[Action] = {Action.NONE}
    if inv.ore >= blueprint.ore_bot_ore_cost and inv.ore_bots < blueprint.max_ore_cost:
        possible_actions.add(Action.ORE)
    if inv.ore >= blueprint.clay_bot_ore_cost and inv.clay_bots < blueprint.max_clay_cost:
        possible_actions.add(Action.CLAY)
    if inv.ore >= blueprint.obs_bot_ore_cost and inv.clay >= blueprint.obs_bot_clay_cost and inv.obs_bots < blueprint.max_obs_cost:
        possible_actions.add(Action.OBS)
    if inv.ore >= blueprint.geo_bot_ore_cost and inv.obs >= blueprint.geo_bot_obs_cost:
        possible_actions.add(Action.GEO)

    return possible_actions


def get_blueprint_score(blueprint: Blueprint, minutes: int) -> int:
    """Get the best number of geodes possible from a blueprint"""
    # Always start with 1 ord producing robot and nothing else
    best: list[InventoryWithForbiddenActions] = [InventoryWithForbiddenActions(Inventory(1, 0, 0, 0, 0, 0, 0, 0), set())]

    for minute in range(minutes):
        new_best: list[InventoryWithForbiddenActions] = []
        for inv in best:
            possible_actions = _possible_actions(inv.inv, blueprint)
            if minute == minutes - 1:
                # Final minute, no point building any more bots:
                possible_actions &= {Action.NONE}
            elif minute == minutes - 2:
                # Penultimate minute - only thing to do is build a geo robot (if we can)
                possible_actions &= {Action.NONE, Action.GEO}
            elif minute == minutes - 3:
                # Anti-penultimate minute - only thing to do is build a geo robot (if we can)
                possible_actions &= {Action.NONE, Action.GEO}

            if Action.GEO in possible_actions:
                # If you can build a geode bot, do it!
                new_best.append(InventoryWithForbiddenActions(_apply_action(inv.inv, blueprint, Action.GEO), set()))
            elif Action.OBS in possible_actions:
                # If you can build a obs bot, do it!
                new_best.append(InventoryWithForbiddenActions(_apply_action(inv.inv, blueprint, Action.OBS), set()))
            else:
                for action in possible_actions:
                    if action == Action.NONE:
                        new_best.append(InventoryWithForbiddenActions(_apply_action(inv.inv, blueprint, Action.NONE), possible_actions - {Action.NONE}))
                    if action == Action.ORE and Action.ORE not in inv.forbidden_actions:
                        new_best.append(InventoryWithForbiddenActions(_apply_action(inv.inv, blueprint, Action.ORE), set()))
                    if action == Action.CLAY and Action.CLAY not in inv.forbidden_actions:
                        new_best.append(InventoryWithForbiddenActions(_apply_action(inv.inv, blueprint, Action.CLAY), set()))
        best = new_best
        # print(minute)
        # print(f"{len(best)} candidates")

    # breakpoint()
    return max(inv.inv.geo for inv in best)

def part1(ll: list[str], args=None) -> str:
    del args

    MINUTES = 24

    quality = 0
    for l in ll:
        params = get_numbers(l)
        blueprint_index = params[0]
        blueprint = Blueprint(params[1], params[2], params[3], params[4], params[5], params[6])
        # print(blueprint)
        quality += blueprint_index * get_blueprint_score(blueprint, MINUTES)
    return str(quality)

def part2(ll: list[str], args=None) -> str:
    del args
    MINUTES = 32
    quality = 1
    for l in islice(ll, 3):
        params = get_numbers(l)
        blueprint = Blueprint(params[1], params[2], params[3], params[4], params[5], params[6])
        quality *= get_blueprint_score(blueprint, MINUTES)
    return str(quality)
