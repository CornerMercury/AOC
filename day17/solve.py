from aocd import get_data, submit
from heapq import heappop, heappush

YEAR = 2023


def part1(data):
    grid = [[c for c in row] for row in data.split("\n")]
    poses = {}
    q = [(0, (0, 0), (0, 0), 0)]
    min_end = 999999999999999
    while q:
        loss, pos, d, straight_steps = heappop(q)
        key = (pos, d, straight_steps)
        if key in poses and poses[key] <= loss:
            continue
        poses[key] = loss

        if pos == (len(grid) - 1, len(grid[0]) - 1):
            min_end = min(min_end, loss)

        for new_d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if new_d == (-d[0], -d[1]):
                continue
            new_pos = pos[0] + new_d[0], pos[1] + new_d[1]
            if not (0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0])):
                continue
            new_steps = 1
            if new_d == d:
                if straight_steps >= 3:
                    continue
                new_steps = straight_steps + 1

            heappush(
                q, (loss + int(grid[new_pos[0]][new_pos[1]]), new_pos, new_d, new_steps)
            )
    return min_end


def part2(data):
    grid = [[c for c in row] for row in data.split("\n")]
    poses = {}
    q = [(0, (0, 0), (0, 0), 0)]
    min_end = 999999999999999
    while q:
        loss, pos, d, straight_steps = heappop(q)
        key = (pos, d, straight_steps)
        if key in poses and poses[key] <= loss:
            continue
        poses[key] = loss

        if pos == (len(grid) - 1, len(grid[0]) - 1) and straight_steps >= 4:
            min_end = min(min_end, loss)

        for new_d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if new_d == (-d[0], -d[1]):
                continue
            new_pos = pos[0] + new_d[0], pos[1] + new_d[1]
            if not (0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0])):
                continue
            new_steps = 1
            if new_d == d:
                if straight_steps >= 10:
                    continue
                new_steps = straight_steps + 1
            elif straight_steps < 4 and d != (0, 0):
                continue
            heappush(
                q, (loss + int(grid[new_pos[0]][new_pos[1]]), new_pos, new_d, new_steps)
            )
    return min_end


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
