from os.path import dirname, join
from dataclasses import dataclass
from typing import NamedTuple
from copy import copy


@dataclass
class State:
    time_remaining: int
    ore_robots: int = 1
    clay_robots: int = 0
    obsidian_robots: int = 0
    geode_robots: int = 0
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geodes: int = 0

    def tick(self):
        self.ore += self.ore_robots
        self.clay += self.clay_robots
        self.obsidian += self.obsidian_robots
        self.geodes += self.geode_robots
        self.time_remaining -= 1

    def can_beat(self, max_geodes):
        extra_geodes = (
            self.time_remaining * self.geode_robots
            + self.time_remaining * (self.time_remaining - 1) // 2
        )
        return self.geodes + extra_geodes > max_geodes

    def can_build_ore(self, blueprint):
        return self.ore >= blueprint.ore_robot.ore

    def can_build_clay(self, blueprint):
        return self.ore >= blueprint.clay_robot.ore

    def can_build_obsidian(self, blueprint):
        return (
            self.ore >= blueprint.obsidian_robot.ore
            and self.clay >= blueprint.obsidian_robot.clay
        )

    def can_build_geode(self, blueprint):
        return (
            self.ore >= blueprint.geode_robot.ore
            and self.obsidian >= blueprint.geode_robot.obsidian
        )

    def build_ore(self, blueprint):
        self.ore -= blueprint.ore_robot.ore
        self.ore_robots += 1

    def build_clay(self, blueprint):
        self.ore -= blueprint.clay_robot.ore
        self.clay_robots += 1

    def build_obsidian(self, blueprint):
        self.ore -= blueprint.obsidian_robot.ore
        self.clay -= blueprint.obsidian_robot.clay
        self.obsidian_robots += 1

    def build_geode(self, blueprint):
        self.ore -= blueprint.geode_robot.ore
        self.obsidian -= blueprint.geode_robot.obsidian
        self.geode_robots += 1


class Materials(NamedTuple):
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0


class Blueprint(NamedTuple):
    ore_robot: Materials
    clay_robot: Materials
    obsidian_robot: Materials
    geode_robot: Materials


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./19i.txt")

    with open(path) as f:
        lines = [
            [robot.split() for robot in line.strip("\n").split(".")]
            for line in f.readlines()
        ]

    return [
        Blueprint(
            Materials(int(blueprint[0][6])),
            Materials(int(blueprint[1][4])),
            Materials(int(blueprint[2][4]), int(blueprint[2][7])),
            Materials(int(blueprint[3][4]), 0, int(blueprint[3][7])),
        )
        for blueprint in lines
    ]


def find_max_geodes(bp, state=State(24), result=0):
    if state.time_remaining == 0:
        return state.geodes

    if state.can_build_geode(bp):
        new_state = copy(state)
        new_state.tick()
        new_state.build_geode(bp)
        if new_state.can_beat(result):
            result = max(result, find_max_geodes(bp, new_state, result))
    if state.can_build_ore(bp):
        new_state = copy(state)
        new_state.tick()
        new_state.build_ore(bp)
        if new_state.can_beat(result):
            result = max(result, find_max_geodes(bp, new_state, result))
    if state.can_build_clay(bp):
        new_state = copy(state)
        new_state.tick()
        new_state.build_clay(bp)
        if new_state.can_beat(result):
            result = max(result, find_max_geodes(bp, new_state, result))
    if state.can_build_obsidian(bp):
        new_state = copy(state)
        new_state.tick()
        new_state.build_obsidian(bp)
        if new_state.can_beat(result):
            result = max(result, find_max_geodes(bp, new_state, result))

    new_state = copy(state)
    new_state.tick()
    result = max(result, find_max_geodes(bp, new_state, result))
    return result


def main():
    for blueprint in get_data():
        print(find_max_geodes(blueprint))


if __name__ == "__main__":
    main()
