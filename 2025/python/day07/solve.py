from aocd import get_data, submit
from collections import Counter

YEAR = 2025


def part1(data):
    l = data.split("\n")
    s = set()
    s.add((0,l[0].index("S")))
    t = 0
    while s:
        new_s = set()
        for y,x in s:
            if y + 1 >= len(l):
                continue
            if l[y + 1][x] == "^":
                t += 1
                if x - 1 >= 0:
                    new_s.add((y + 1, x - 1))
                if x + 1 < len(l[0]):
                    new_s.add((y + 1, x + 1))
            else:
                new_s.add((y + 1, x))
        s = new_s

    return t


def part2(data):
    l = data.split("\n")
    s = Counter()
    s[(0,l[0].index("S"))] += 1
    t = 0
    while True:
        new_s = Counter()
        for p,c in s.items():
            y,x = p
            if y + 1 >= len(l):
                continue
            if l[y + 1][x] == "^":
                if x - 1 >= 0:
                    new_s[(y + 1, x - 1)] += c
                if x + 1 < len(l[0]):
                    new_s[(y + 1, x + 1)] += c
            else:
                new_s[(y + 1, x)] += c
        s = new_s
        if y + 1 == len(l[0]) - 1:
            return sum(s.values())


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
