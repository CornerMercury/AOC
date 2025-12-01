from aocd import get_data, submit

YEAR = 2023


def part1(data):
    grid = [[c for c in row] for row in data.split("\n")]
    for y, row in enumerate(grid):
        if y == 0:
            continue
        for x, c in enumerate(row):
            if c == "O":
                ny = y
                while ny > 0 and grid[ny - 1][x] == ".":
                    grid[ny - 1][x] = "O"
                    grid[ny][x] = "."
                    ny -= 1

    res = 0
    for y, row in enumerate(grid):
        for c in row:
            if c == "O":
                res += len(grid) - y
    return res


def tilt(grid):
    for y, row in enumerate(grid):
        if y == 0:
            continue
        for x, c in enumerate(row):
            if c == "O":
                ny = y
                while ny > 0 and grid[ny - 1][x] == ".":
                    grid[ny - 1][x] = "O"
                    grid[ny][x] = "."
                    ny -= 1

    return grid


def part2(data):
    grid = [[c for c in row] for row in data.split("\n")]
    grid = tuple(map(tuple, grid))
    states = [grid]
    states_set = set()
    for _ in range(1000000000):
        grid = list(map(list, grid))
        grid = tilt(grid)
        grid = list(map(list, zip(*grid[::-1])))
        grid = tilt(grid)
        grid = list(map(list, zip(*grid[::-1])))
        grid = tilt(grid)
        grid = list(map(list, zip(*grid[::-1])))
        grid = tilt(grid)
        grid = list(map(list, zip(*grid[::-1])))
        grid = tuple(map(tuple, grid))
        if grid not in states_set:
            states_set.add(grid)
            states.append(grid)
        else:
            break
    offset = states.index(grid)
    cycle = len(states) - offset
    states.append(grid)
    grid = states[(1000000000 - offset) % cycle + offset]
    res = 0
    for y, row in enumerate(grid):
        for c in row:
            if c == "O":
                res += len(grid) - y
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
