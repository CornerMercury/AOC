from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    map = [[int(l[y][x]) if l[y][x].isdigit() else l[y][x] for x in range(len(l[0]))] for y in range(len(l))]

    def r(y, x, intended):
        if not (0 <= y < len(map) and 0 <= x < len(map[0])):
            return set()
        if intended != map[y][x]:
            return set()
        if map[y][x] == 9:
            return {(y, x)}

        i = map[y][x] + 1
        return r(y - 1, x, i) | r(y + 1, x, i) | r(y, x - 1, i) | r(y, x + 1, i)

    t = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            t += len(r(y, x, 0))

    return t


def part2(data):
    l = data.split("\n")
    map = [[int(l[y][x]) if l[y][x].isdigit() else l[y][x] for x in range(len(l[0]))] for y in range(len(l))]

    def r(y, x, intended):
        if not (0 <= y < len(map) and 0 <= x < len(map[0])):
            return 0
        if intended != map[y][x]:
            return 0
        if map[y][x] == 9:
            return 1

        i = map[y][x] + 1
        return r(y - 1, x, i) + r(y + 1, x, i) + r(y, x - 1, i) + r(y, x + 1, i)

    t = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            t += r(y, x, 0)

    return t


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
