from aocd import get_data, submit

YEAR = 2023


def adjacent_digits(grid, n, row_length):
    poses = []
    for d in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        try:
            char = grid[y + d[0]][x + d[1]]
            if char.isdigit():
                poses.append((y + d[0], x + d[1]))
        except IndexError:
            continue
    return poses


def part1(data):
    row_len = data.find("\n") + 1
    num_set = set()
    res = 0
    for i in range(len(data)):
        if data[i] not in ".123456789":
            for yn, xn in adjacent_digits(
                data,
                i,
            ):
                s = ""
                while 0 <= xn and grid[yn][xn].isdigit():
                    xn -= 1
                xn += 1
                if (yn, xn) in num_set:
                    continue

                num_set.add((yn, xn))

                while grid[yn][xn].isdigit():
                    s += grid[yn][xn]
                    xn += 1

                res += int(s)

    print(res)


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
