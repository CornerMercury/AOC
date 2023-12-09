from aocd import get_data, submit
from math import lcm

YEAR = 2023


def part1(data):
    inst, _, *l = data.split("\n")
    paths = {}
    for line in l:
        key, values = line.split(" = ")
        values = values[1:-1].split(", ")
        paths[key] = tuple(values)

    node = "AAA"
    count = 0
    i = 0
    while node != "ZZZ":
        out = paths[node]
        node = out["LR".index(inst[i])]
        count += 1
        i = (i + 1) % len(inst)
    return count


def find_cycle(node, inst, paths):
    visited = {}
    i = 0
    last_z = 0
    while (node, i % len(inst)) not in visited:
        visited[node, i % len(inst)] = i
        node = paths[node]["LR".index(inst[i % len(inst)])]
        i += 1
        if node[-1] == "Z":
            last_z = i

    # offsets are all zero??
    return i - visited[node, i % len(inst)]


def part2(data):
    inst, _, *l = data.split("\n")
    paths = {}
    nodes = []
    for line in l:
        key, values = line.split(" = ")
        values = values[1:-1].split(", ")
        paths[key] = tuple(values)
        if key[-1] == "A":
            nodes.append(key)

    periods = [find_cycle(node, inst, paths) for node in nodes]
    return lcm(*periods)


def main():
    day = int(__file__.split("\\")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
