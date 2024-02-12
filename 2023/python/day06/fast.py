from aocd import get_data, submit
import math

YEAR = 2023


def part1(data):
    t, d = map(lambda x: map(int, x.split(":")[1].split()), data.split("\n"))
    res = 1
    for x, m in zip(t, d):
        discrim = math.sqrt(x**2 - 4 * m)
        sol1 = (x - discrim) / 2
        sol2 = (x + discrim) // 2
        wins = int(sol2) - math.ceil(sol1)
        wins += -1 if sol1.is_integer() else 1
        res *= wins

    return res


def part2(data):
    x, m = map(lambda x: int("".join(x.split(":")[1].split())), data.split("\n"))
    discrim = math.sqrt(x**2 - 4 * m)
    sol1 = (x - discrim) / 2
    sol2 = (x + discrim) // 2
    wins = int(sol2) - math.ceil(sol1)
    wins += -1 if sol1.is_integer() else 1
    return wins


data = """Time:      7  15   30
Distance:  9  40  200"""


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
