from aocd import get_data, submit
from collections import Counter

YEAR = 2025


def part1(data):
    l = data.split("\n")
    s = set()
    s.add((0, l[0].index("S")))
    t = 0
    while s:
        new_s = set()
        for y, x in s:
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
    l=data.split()
    s={data.find('S'):1}
    for r in l[1:]:
        n={}
        for p in s:
            for d in range(-(r[p]>'A'),2,2):k=p+d;n[k]=n.get(k,0)+s[p]
        s=n
    print(sum(s.values()))


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
