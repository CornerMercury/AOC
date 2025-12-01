from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    G = {}
    for s in l:
        a, b = s.split('-')
        if a not in G:
            G[a] = []
        if b not in G:
            G[b] = []
        G[a].append(b)
        G[b].append(a)
    
    lans = set()
    for node, adjacents in G.items():
        if node[0] != 't':
            continue
        for adjacent_1 in adjacents:
            for adjacent_2 in G[adjacent_1]:
                for adjacent_3 in G[adjacent_2]:
                    if adjacent_3 == node:
                        lans.add(tuple(sorted([node, adjacent_1, adjacent_2])))

    return len(lans)

def part2(data):
    l = data.split("\n")
    G = {}
    for s in l:
        a, b = s.split('-')
        if a not in G:
            G[a] = set()
        if b not in G:
            G[b] = set()
        G[a].add(b)
        G[b].add(a)
    
    def BronKerbosch1(R, P, X, max_clique=[]):
        if len(P) == 0 and len(X) == 0 and len(R) > len(max_clique): 
            max_clique = list(R)
        for v in list(P):
            max_clique = BronKerbosch1(R | {v}, P & G[v], X & G[v], max_clique)
            P -= {v}
            X |= {v}
        return max_clique
     
    return ','.join(sorted(BronKerbosch1(set(), G.keys(), set())))


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
