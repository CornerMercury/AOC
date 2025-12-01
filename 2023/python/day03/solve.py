from aocd import get_data, submit

YEAR = 2023


def is_adjacent_symbol(grid, y, x):
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        try:
            char = grid[y + d[0]][x + d[1]]
            if char != "." and not char.isdigit():
                return True, (char == "*") * (y + d[0], x + d[1])
        except IndexError:
            continue
    return False, ()


def part1(data):
    grid = [[c for c in line] for line in data.split("\n")]
    res = 0
    s = ""
    symbol = False
    for y in range(len(grid)):
        if s and symbol:
            res += int(s)
        s = ""
        symbol = False
        for x in range(len(grid[y])):
            c = grid[y][x]
            if c.isdigit():
                s += c
                symbol |= is_adjacent_symbol(grid, y, x)[0]
            else:
                if s and symbol:
                    res += int(s)
                s = ""
                symbol = False


def part2(data):
    grid = [[c for c in line] for line in data.split("\n")]
    s = ""
    gears = set()
    gear_poses = {}
    for y in range(len(grid)):
        if s and gears:
            for gear in gears:
                if gear in gear_poses:
                    gear_poses[gear].append(int(s))
                else:
                    gear_poses[gear] = [int(s)]

        s = ""
        gears = set()
        for x in range(len(grid[y])):
            c = grid[y][x]
            if c.isdigit():
                s += c
                _, gear_pos = is_adjacent_symbol(grid, y, x)
                if gear_pos:
                    gears.add(gear_pos)
            else:
                if s and gears:
                    for gear in gears:
                        if gear in gear_poses:
                            gear_poses[gear].append(int(s))
                        else:
                            gear_poses[gear] = [int(s)]

                s = ""
                gears = set()

    return sum(v[0] * v[1] for _, v in gear_poses.items() if len(v) == 2)


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
