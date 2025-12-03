from aocd import get_data, submit
import re

YEAR = 2025


def part1(data):
    l = data.strip("\n")
    t = 0
    for r in l.split(","):
        left, right = map(int, r.split("-"))
        for n in range(left, right + 1):
            s_n = str(n)
            if s_n[: len(s_n) // 2] == s_n[len(s_n) // 2 :]:
                t += n

    return t


def part2(data):
    l = data.strip("\n")
    t = 0
    for r in l.split(","):
        left, right = map(int, r.split("-"))
        for n in range(left, right + 1):
            s_n = str(n)
            if re.search(r"^(.+)\1+$", s_n):
                t += n
    return t


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
