from aocd import get_data, submit
from collections import deque

YEAR = 2023


def part1(data):
    l = data.split("\n")
    poses = set([0])
    pos = 0
    for line in l:
        d, n, _ = line.split()
        d = (1j, 1, -1j, -1)["RDLU".index(d)]
        for _ in range(int(n)):
            pos += d
            poses.add(pos)

    # assumes (1, 1) is in hole
    s = deque()
    s.append(1 + 1j)
    while s:
        current = s.pop()
        if current in poses:
            continue
        poses.add(current)
        for d in (1j, 1, -1j, -1):
            s.append(current + d)

    return len(poses)


def part2(data):
    l = data.split("\n")
    poses = []
    pos = 0
    res = 2
    for line in l:
        _, _, h = line.split()
        n = int(h[2:-1], 16) >> 4
        d = (1j, 1, -1j, -1)["0123".index(h[-2])]
        pos += d * n
        res += n
        poses.append(pos)

    # shoelace formula
    for i in range(len(poses) - 1):
        res += int(
            (poses[i].real + poses[i + 1].real) * (poses[i].imag - poses[i + 1].imag)
        )

    return res // 2


data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


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
