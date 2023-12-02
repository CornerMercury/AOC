from aocd import get_data, submit

DAY = 2
YEAR = 2023


def part1(l):
    res = 0
    for s in l:
        id, cubes = s.split(":")
        id = int(id.split()[1])
        sets = cubes.split(";")
        b = False
        for set in sets:
            colours = set.split(",")
            for colour in colours:
                n, colour = colour.split()
                n = int(n)
                if colour == "red" and n > 12:
                    b = True
                if colour == "green" and n > 13:
                    b = True
                if colour == "blue" and n > 14:
                    b = True
        if not b:
            res += id

    return res


def part2(l):
    res = 0
    for s in l:
        id, cubes = s.split(":")
        id = int(id.split()[1])
        sets = cubes.split(";")
        maxs = [0, 0, 0]
        for set in sets:
            colours = set.split(",")
            for colour in colours:
                n, colour = colour.split()
                n = int(n)
                if colour == "red" and n > maxs[0]:
                    maxs[0] = n
                if colour == "green" and n > maxs[1]:
                    maxs[1] = n
                if colour == "blue" and n > maxs[2]:
                    maxs[2] = n
        res += maxs[0] * maxs[1] * maxs[2]
    return res


def main():
    data = get_data(day=DAY, year=YEAR)
    lst = data.split("\n")
    p1 = part1(lst)
    if p1:
        submit(p1, part="a", day=DAY, year=YEAR)
    p2 = part2(lst)
    if p2:
        submit(p2, part="b", day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
