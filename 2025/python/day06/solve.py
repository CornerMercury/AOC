from aocd import get_data, submit

YEAR = 2025


def part1(data):
    l = [r.split() for r in data.split("\n")]#
    t = 0
    for c in zip(*l[::-1]):
        t += eval(c[0].join(c[1:]))
    return t


def part2(data):
    l = data.split("\n")
    o = []
    op = l[len(l)-1][0]
    temp = []
    for col in range(len(l[0])):
        n = "".join(l[row][col] for row in range(len(l)-1) if l[row][col] != " ")
        if n == "":
            temp += [op]
            o.append(temp)
            op = l[len(l)-1][col + 1]
            temp = []
            continue
        temp.append(n)
            

    temp += [op]
    o.append(temp)

    t = 0
    for c in o:
        t += eval(c[-1].join(c[:-1]))
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
