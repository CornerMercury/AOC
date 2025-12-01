from aocd import get_data, submit

YEAR = 2023


def part1(data):
    l = data.split("\n")
    universes = []
    cols = set()
    rows = set()
    for y, row in enumerate(l):
        for x, char in enumerate(row):
            if char == "#":
                universes.append((y, x))
                cols.add(x)
                rows.add(y)

    res = 0
    for i, universe1 in enumerate(universes):
        for universe2 in universes[i:]:
            r1, r2 = sorted([universe1[0], universe2[0]])
            c1, c2 = sorted([universe1[1], universe2[1]])
            res += c2 - c1 + r2 - r1
            for r in range(r1, r2):
                if r not in rows:
                    res += 1
            for c in range(c1, c2):
                if c not in cols:
                    res += 1

    return res


def part2(data):
    l = data.split("\n")
    universes = []
    cols = set()
    rows = set()
    for y, row in enumerate(l):
        for x, char in enumerate(row):
            if char == "#":
                universes.append((y, x))
                cols.add(x)
                rows.add(y)

    res = 0
    offset = 1000000
    for i, universe1 in enumerate(universes):
        for universe2 in universes[i:]:
            r1, r2 = sorted([universe1[0], universe2[0]])
            c1, c2 = sorted([universe1[1], universe2[1]])
            res += c2 - c1 + r2 - r1
            for r in range(r1, r2):
                if r not in rows:
                    res += offset - 1
            for c in range(c1, c2):
                if c not in cols:
                    res += offset - 1

    return res


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
