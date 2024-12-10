from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    nodes = set()
    for s in l:
        for c in s:
            nodes |= {c}
    nodes.discard(".")
    antinodes = set()
    for node in nodes:
        poses = []
        for y in range(len(l)):
            for x in range(len(l[0])):
                if l[y][x] == node:
                    poses += [(y,x)]
        for i in range(len(poses)):
            for j in range(i+1, len(poses)):
                y1, x1 = poses[i]
                y2, x2 = poses[j]
                dy, dx = y2-y1, x2-x1
                if 0 <= (y1 - dy) < len(l) and 0 <= (x1 - dx) < len(l[0]):
                    antinodes.add((y1 - dy, x1 - dx))
                if 0 <= (y2 + dy) < len(l) and 0 <= (x2 + dx) < len(l[0]):
                    antinodes.add((y2 + dy, x2 + dx))
    return len(antinodes)


def part2(data):
    l = data.split("\n")
    nodes = set()
    for s in l:
        for c in s:
            nodes |= {c}
    nodes.discard(".")
    antinodes = set()
    for node in nodes:
        poses = []
        for y in range(len(l)):
            for x in range(len(l[0])):
                if l[y][x] == node:
                    poses += [(y,x)]
        for i in range(len(poses)):
            for j in range(i+1, len(poses)):
                y1, x1 = poses[i]
                y2, x2 = poses[j]
                dy, dx = y2-y1, x2-x1
                while 0 <= y1 < len(l) and 0 <= x1 < len(l[0]):
                    antinodes.add((y1, x1))
                    y1 -= dy
                    x1 -= dx
                while 0 <= y2 < len(l) and 0 <= x2 < len(l[0]):
                    antinodes.add((y2, x2))
                    y2 += dy
                    x2 += dx
    return len(antinodes)


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
