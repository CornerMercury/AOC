from aocd import get_data, submit

YEAR = 2025


def part1(data):
    l = data.split("\n")
    d=50
    t=0
    for n in l:
        d = (d+int(n[1:])*(1-2*(n[0]=="L")))%100
        if d == 0:
            t += 1

    return t


def part2(data):
    l = data.split("\n")
    d=50
    t=0
    for n in l:
        dr = 1-2*(n[0]=="L")
        for _ in range(int(n[1:])):
            d = (d+dr)%100
            if d == 0:
                t += 1
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
