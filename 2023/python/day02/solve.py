from aocd import get_data, submit

YEAR = 2023


def part1(data):
    l = data.split("\n")
    res = 0
    for s in l:
        id, cubes = s.split(":")
        id = int(id.split()[1])
        sets = cubes.split(";")
        b = True
        for set in sets:
            colours = set.split(",")
            for colour in colours:
                n, colour = colour.split()
                n = int(n)
                if colour == "red" and n > 12:
                    b = False
                if colour == "green" and n > 13:
                    b = False
                if colour == "blue" and n > 14:
                    b = False
        res += b * id
    return res


def part2(data):
    l = data.split("\n")
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
