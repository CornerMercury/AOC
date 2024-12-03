from aocd import get_data, submit

YEAR = 2023


def part1(data):
    grid = [[c for c in line] for line in data.split("\n")]
    mid = len(grid[0]) // 2
    grid[mid][mid] = "."
    parities = [set(), set()]
    poses = [complex(mid, mid)]
    next_poses = []
    for i in range(64):
        for pos in poses:
            for d in (1, 1j, -1, -1j):
                new_pos = pos + d
                if not (
                    0 <= new_pos.real < len(grid) and 0 <= new_pos.imag < len(grid[0])
                ):
                    continue
                if grid[int(new_pos.real)][int(new_pos.imag)] != ".":
                    continue
                if new_pos in parities[i % 2]:
                    continue
                parities[i % 2].add(new_pos)
                next_poses.append(new_pos)

        poses = next_poses
        next_poses = []

    return len(parities[i % 2])


def part2(data):
    grid = [[c for c in line] for line in data.split("\n")]
    mid = len(grid[0]) // 2
    grid[mid][mid] = "."
    parities = [set(), set()]
    poses = [complex(mid, mid)]
    next_poses = []
    for i in range(mid):
        for pos in poses:
            for d in (1, 1j, -1, -1j):
                new_pos = pos + d
                if grid[int(new_pos.real)][int(new_pos.imag)] != ".":
                    continue
                if new_pos in parities[i % 2]:
                    continue
                parities[i % 2].add(new_pos)
                next_poses.append(new_pos)
        poses = next_poses
        next_poses = []
    corner_parities = [set(), set()]
    for i in range(mid, mid * 2 + 1):
        for pos in poses:
            for d in (1, 1j, -1, -1j):
                new_pos = pos + d
                if not (
                    0 <= new_pos.real < len(grid) and 0 <= new_pos.imag < len(grid[0])
                ):
                    continue
                if grid[int(new_pos.real)][int(new_pos.imag)] != ".":
                    continue
                if new_pos in corner_parities[i % 2] or new_pos in parities[i % 2]:
                    continue
                corner_parities[i % 2].add(new_pos)
                next_poses.append(new_pos)
        poses = next_poses
        next_poses = []
    steps = 26501365
    n = (steps - mid) // 131
    even_square = len(parities[0]) + len(corner_parities[0])
    odd_square = len(parities[1]) + len(corner_parities[1])
    even_corners, odd_corners = map(len, corner_parities)
    return (
        (n + 1) ** 2 * even_square
        + n**2 * odd_square
        - (n + 1) * even_corners
        + n * odd_corners
    )


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
