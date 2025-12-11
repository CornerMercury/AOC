from aocd import get_data, submit
from collections import deque

YEAR = 2025


def part1(data):
    l = data.split("\n")
    g = {}
    indegree = {}
    for line in l:
        s, e = line.split(":")
        indegree[s] = indegree.get(s, 0)
        es = e.split()
        for e in es:
            g[e] = g.get(e, [])
            g[s] = g.get(s, []) + [e]
            indegree[e] = indegree.get(e, 0) + 1
    
    q = deque()
    for node, val in indegree.items():
        if val == 0:
            q.append(node)
    

    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for e in g[node]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)
    
    ways = {node:0 for node in g}
    ways["you"] = 1

    for node in order:
        for e in g[node]:
            ways[e] += ways[node]

    return ways["out"]


def part2(data):
    l = data.split("\n")
    g = {}
    indegree = {}
    for line in l:
        s, e = line.split(":")
        indegree[s] = indegree.get(s, 0)
        es = e.split()
        for e in es:
            g[e] = g.get(e, [])
            g[s] = g.get(s, []) + [e]
            indegree[e] = indegree.get(e, 0) + 1
    
    q = deque()
    for node, val in indegree.items():
        if val == 0:
            q.append(node)
    

    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for e in g[node]:
            indegree[e] -= 1
            if indegree[e] == 0:
                q.append(e)
    
    first = ["fft", "dac"][order.index("fft") > order.index("dac")]
    second = ["fft", "dac"][order.index("fft") < order.index("dac")]
    ways = {node:0 for node in g}
    ways["svr"] = 1

    for node in order:
        for e in g[node]:
            ways[e] += ways[node]
    
    ways_to_first = ways[first]
    ways = {node:0 for node in g}
    ways[first] = ways_to_first
    for node in order:
        for e in g[node]:
            ways[e] += ways[node]
    
    ways_to_second = ways[second]
    ways = {node:0 for node in g}
    ways[second] = ways_to_second
    for node in order:
        for e in g[node]:
            ways[e] += ways[node]

    return ways["out"]


def main():
    day = int(__file__.split("/")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
