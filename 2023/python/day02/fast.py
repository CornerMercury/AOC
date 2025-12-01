from aocd import get_data, submit

YEAR = 2023


def part1(data):
    res = 0
    for line in data.split("\n"):
        id, cubes = line.split(":")
        b = 1
        for set in cubes.split(";"):
            for colour in set.split(","):
                n, colour = colour.split()
                n = int(n)
                match colour:
                    case "red":
                        if n > 12:
                            b = 0
                    case "green":
                        if n > 13:
                            b = 0
                    case "blue":
                        if n > 14:
                            b = 0
        res += b * int(id[5:])
    return res


def part2(data):
    res = 0
    for line in data.split("\n"):
        for set in line.split(":")[1].split(";"):
            red = green = blue = 0
            for colour in set.split(","):
                n, colour = colour.split()
                n = int(n)
                match colour:
                    case "red":
                        red = max(red, n)
                    case "green":
                        green = max(green, n)
                    case "blue":
                        blue = max(blue, n)

        res += red * green * blue
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
