from aocd import get_data, submit
import networkx as nx
from random import choice

YEAR = 2023


def part1(data):
    l = data.split("\n")
    graph = nx.Graph()
    for line in l:
        key, connections = line.split(": ")
        connections = connections.split()
        for node in connections:
            graph.add_edge(key, node, capacity=1)

    cut = 4
    while cut > 3:
        s = choice(list(graph.nodes))
        e = choice(list(graph.nodes))
        cut, subsets = nx.minimum_cut(graph, s, e, capacity='capacity')
        if cut == 3:
            return len(subsets[0]) * len(subsets[1])



def part2(data):
    l = data.split("\n")
    return None


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
