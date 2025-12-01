from aocd import get_data, submit
from collections import deque

YEAR = 2023


def part1(data):
    grid = tuple(tuple(c for c in row) for row in data.split("\n"))
    tile_set = set()
    move_set = set()
    stack = deque()
    stack.append(((0, 0), (0, 1)))
    while stack:
        pos, dir = stack.pop()
        if not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
            continue
        if pos not in tile_set:
            tile_set.add(pos)
        elif (pos, dir) in move_set:
            continue

        move_set.add((pos, dir))

        match grid[pos[0]][pos[1]]:
            case ".":
                stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "/":
                dir = (dir[1] * -1, dir[0] * -1)
                stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "\\":
                dir = (dir[1], dir[0])
                stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "|":
                if dir[1] == 0:
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                else:
                    dir = (1, 0)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                    dir = (-1, 0)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "-":
                if dir[0] == 0:
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                else:
                    dir = (0, 1)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                    dir = (0, -1)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
    return len(tile_set)


max_count = 0


def get_elec(grid, start_pos, start_dir):
    tile_set = set()
    move_set = set()
    stack = deque()
    stack.append((start_pos, start_dir))
    count = 0
    while stack:
        count += 1
        pos, dir = stack.pop()
        if not (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
            continue
        if pos not in tile_set:
            tile_set.add(pos)
        elif (pos, dir) in move_set:
            continue

        move_set.add((pos, dir))

        match grid[pos[0]][pos[1]]:
            case ".":
                stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "/":
                dir = (dir[1] * -1, dir[0] * -1)
                stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "\\":
                dir = (dir[1], dir[0])
                stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "|":
                if dir[1] == 0:
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                else:
                    dir = (1, 0)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                    dir = (-1, 0)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
            case "-":
                if dir[0] == 0:
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                else:
                    dir = (0, 1)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
                    dir = (0, -1)
                    stack.append(((pos[0] + dir[0], pos[1] + dir[1]), dir))
    global max_count
    max_count = max(max_count, count)
    return len(tile_set)


def part2(data):
    grid = tuple(tuple(c for c in row) for row in data.split("\n"))
    max_size = 0
    for i in range(len(grid[0])):
        max_size = max(max_size, get_elec(grid, (0, i), (1, 0)))
        max_size = max(max_size, get_elec(grid, (len(grid) - 1, i), (-1, 0)))

    for i in range(len(grid)):
        max_size = max(max_size, get_elec(grid, (i, 0), (0, 1)))
        max_size = max(max_size, get_elec(grid, (i, len(grid[0]) - 1), (0, -1)))

    return max_size


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
