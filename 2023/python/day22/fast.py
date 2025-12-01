from aocd import get_data, submit

YEAR = 2023


def faces_overlap(brick1, brick2):
    x1, y1, x2, y2 = *brick1[0][:-1], *brick1[1][:-1]
    xx1, yy1, xx2, yy2 = *brick2[0][:-1], *brick2[1][:-1]
    return min(x2, xx2) >= max(x1, xx1) and min(y2, yy2) >= max(y1, yy1)


def drop(bricks, max_height):
    frozen_min_heights = [[] for _ in range(max_height + 1)]
    frozen_max_heights = [[] for _ in range(max_height + 1)]
    while bricks:
        next_bricks = []
        for brick in bricks:
            min_height = brick[0][2]
            if min_height == 1:
                frozen_min_heights[min_height].append(tuple(map(tuple, brick)))
                frozen_max_heights[brick[1][2]].append(tuple(map(tuple, brick)))
            else:
                next_bricks.append(brick)
        bricks = []
        for brick in sorted(next_bricks, key=lambda x: x[0][2]):
            for frozen in frozen_max_heights[brick[0][2] - 1]:
                if faces_overlap(brick, frozen):
                    frozen_min_heights[brick[0][2]].append(tuple(map(tuple, brick)))
                    frozen_max_heights[brick[1][2]].append(tuple(map(tuple, brick)))
                    break
            else:
                brick = [*brick[0][:2], brick[0][2] - 1], [
                    *brick[1][:2],
                    brick[1][2] - 1,
                ]
                bricks.append(brick)

    return frozen_min_heights, frozen_max_heights


def part1(data):
    l = data.split("\n")
    bricks = []
    max_height = 0
    for line in l:
        left, right = line.split("~")
        left = list(map(int, left.split(",")))
        right = list(map(int, right.split(",")))
        max_height = max(max_height, right[2])
        bricks.append(
            (left, right),
        )
    frozen_min_heights, frozen_max_heights = drop(bricks, max_height)
    res = 0
    for belows, aboves in zip(frozen_max_heights, frozen_min_heights[1:]):
        counter = {}
        below_map = {}
        for below in belows:
            below_map[below] = []
            for above in aboves:
                if faces_overlap(below, above):
                    below_map[below].append(above)
                    if above not in counter:
                        counter[above] = 0
                    counter[above] += 1
        for below, aboves in below_map.items():
            if all(counter[above] != 1 for above in aboves):
                res += 1
    return res


def part2(data):
    l = data.split("\n")
    bricks = []
    max_height = 0
    for line in l:
        left, right = line.split("~")
        left = list(map(int, left.split(",")))
        right = list(map(int, right.split(",")))
        max_height = max(max_height, right[2])
        bricks.append(
            (left, right),
        )

    frozen_min_heights, _ = drop(bricks, max_height)
    bs = [brick for height in frozen_min_heights for brick in height]
    res = 0
    for i in range(len(bs)):
        bricks = bs[:i] + bs[i + 1 :]
        frozen_max_heights = [[] for _ in range(max_height + 1)]
        next_bricks = []
        for brick in bricks:
            min_height = brick[0][2]
            if min_height == 1:
                frozen_max_heights[brick[1][2]].append(tuple(map(tuple, brick)))
            else:
                next_bricks.append(brick)
        for brick in sorted(next_bricks, key=lambda x: x[0][2]):
            for frozen in frozen_max_heights[brick[0][2] - 1]:
                if faces_overlap(brick, frozen):
                    frozen_max_heights[brick[1][2]].append(tuple(map(tuple, brick)))
                    break
            else:
                res += 1
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
