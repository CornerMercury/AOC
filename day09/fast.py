from aocd import get_data, submit

YEAR = 2023


def part1(data):
    l = data.split("\n")
    res = 0
    for line in l:
        splits = []
        nums = map(int, line.split())
        splits.append(list(nums))
        while not all(num == 0 for num in splits[-1]):
            splits.append([m - n for n, m in zip(splits[-1], splits[-1][1:])])

        res += sum(map(lambda x: x[-1], splits))

    return res


def part2(data):
    l = data.split("\n")
    res = 0
    for line in l:
        splits = []
        nums = map(int, line.split())
        splits.append(list(nums))
        while not all(num == 0 for num in splits[-1]):
            splits.append([m - n for n, m in zip(splits[-1], splits[-1][1:])])

        count = 0
        for split in splits[::-1]:
            count = split[0] - count
        res += count
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
