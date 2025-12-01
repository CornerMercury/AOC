from aocd import get_data, submit
from queue import SimpleQueue as Queue
from matplotlib.path import Path

YEAR = 2023


def part1(data):
    poses = {}
    grid = [[c for c in line] for line in data.split("\n")]
    next_q = Queue()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "S":
                if x + 1 < len(row) and grid[y][x + 1] in "-J7":
                    next_q.put((y, x + 1))
                if 0 <= x - 1 and grid[y][x - 1] in "-LF":
                    next_q.put((y, x - 1))
                if y + 1 < len(grid) and grid[y + 1][x] in "|JL":
                    next_q.put((y + 1, x))
                if 0 <= y - 1 and grid[y - 1][x] in "|7F":
                    next_q.put((y - 1, x))

    # bfs
    depth = 1
    while not next_q.empty():
        q = next_q
        next_q = Queue()
        while not q.empty():
            y, x = current = q.get()
            if current in poses:
                continue

            poses[current] = depth
            match grid[y][x]:
                case "|":
                    next_q.put((y - 1, x))
                    next_q.put((y + 1, x))
                case "-":
                    next_q.put((y, x - 1))
                    next_q.put((y, x + 1))
                case "L":
                    next_q.put((y - 1, x))
                    next_q.put((y, x + 1))
                case "J":
                    next_q.put((y - 1, x))
                    next_q.put((y, x - 1))
                case "7":
                    next_q.put((y + 1, x))
                    next_q.put((y, x - 1))
                case "F":
                    next_q.put((y + 1, x))
                    next_q.put((y, x + 1))
        depth += 1

    return max(poses.values())


def part2(data):
    poses = set()
    grid = [[c for c in line] for line in data.split("\n")]
    next_q = Queue()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "S":
                if x + 1 < len(row) and grid[y][x + 1] in "-J7":
                    next_q.put((y, x + 1))
                if 0 <= x - 1 and grid[y][x - 1] in "-LF":
                    next_q.put((y, x - 1))
                if y + 1 < len(grid) and grid[y + 1][x] in "|JL":
                    next_q.put((y + 1, x))
                if 0 <= y - 1 and grid[y - 1][x] in "|7F":
                    next_q.put((y - 1, x))
                start = (y, x)

    # bfs
    while not next_q.empty():
        q = next_q
        next_q = Queue()
        while not q.empty():
            y, x = current = q.get()
            if current in poses:
                continue

            poses.add(current)
            match grid[y][x]:
                case "|":
                    next_q.put((y - 1, x))
                    next_q.put((y + 1, x))
                case "-":
                    next_q.put((y, x - 1))
                    next_q.put((y, x + 1))
                case "L":
                    next_q.put((y - 1, x))
                    next_q.put((y, x + 1))
                case "J":
                    next_q.put((y - 1, x))
                    next_q.put((y, x - 1))
                case "7":
                    next_q.put((y + 1, x))
                    next_q.put((y, x - 1))
                case "F":
                    next_q.put((y + 1, x))
                    next_q.put((y, x + 1))

    # construct path
    path = [start]
    y, x = start
    if x + 1 < len(row) and grid[y][x + 1] in "-J7":
        path.append((y, x + 1))
    elif 0 <= x - 1 and grid[y][x - 1] in "-LF":
        path.append((y, x - 1))
    elif y + 1 < len(grid) and grid[y + 1][x] in "|JL":
        path.append((y + 1, x))
    elif 0 <= y - 1 and grid[y - 1][x] in "|7F":
        path.append((y - 1, x))
    y, x = path[-1]
    while len(path) < len(poses):
        last = path[-2]
        match grid[y][x]:
            case "|":
                path.append(list(set([(y - 1, x), (y + 1, x)]) - set([last]))[0])
            case "-":
                path.append(list(set([(y, x - 1), (y, x + 1)]) - set([last]))[0])
            case "L":
                path.append(list(set([(y - 1, x), (y, x + 1)]) - set([last]))[0])
            case "J":
                path.append(list(set([(y - 1, x), (y, x - 1)]) - set([last]))[0])
            case "7":
                path.append(list(set([(y + 1, x), (y, x - 1)]) - set([last]))[0])
            case "F":
                path.append(list(set([(y + 1, x), (y, x + 1)]) - set([last]))[0])
        y, x = path[-1]
    total = 0

    p = Path(path[:-1])
    for y, row in enumerate(grid):
        for x in range(len(row)):
            if (y, x) in poses:
                continue
            total += p.contains_point((y, x))

    return total

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
