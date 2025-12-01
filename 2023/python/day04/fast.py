from aocd import get_data, submit

YEAR = 2023


def part1(data):
    l = data.split("\n")
    res = 0
    for line in l:
        g = line.split(":")[1]
        win_nums, nums = map(str.split, g.split("|"))
        count = -1
        for num in nums:
            if num in win_nums:
                count += 1

        res += 0 if count < 0 else 2**count

    return res


def part2(data):
    l = data.split("\n")
    all_cards = {}
    res = 0
    for line in l:
        id, g = line.split(":")
        id = int(id.split()[1])
        win_nums, nums = map(str.split, g.split("|"))
        count = 0
        for num in nums:
            if num in win_nums:
                count += 1

        if id not in all_cards:
            prod = 1
        else:
            prod = all_cards[id] + 1
        res += prod
        for i in range(1, count + 1):
            if id + i in all_cards:
                all_cards[id + i] += prod
            else:
                all_cards[id + i] = prod

    return res


def main():
    day = int(__file__.split("\\")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    print(p2)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
