from aocd import get_data, submit

YEAR = 2023


def adjacent_digits(s, n, row_length):
    poses = []
    for d in [
        -row_length - 1,
        -row_length,
        -row_length + 1,
        -1,
        1,
        row_length - 1,
        row_length,
        row_length + 1,
    ]:
        new_index = n + d
        if 0 <= new_index < len(s) and s[new_index].isdigit():
            poses.append(new_index)
    return poses


def part1(data):
    row_len = data.find("\n") + 1
    pos_set = set()
    res = 0
    for i in range(len(data)):
        if data[i] not in ".1234567890\n":
            for n in adjacent_digits(data, i, row_len):
                s = ""
                while 0 <= n and data[n].isdigit():
                    n -= 1
                n += 1
                if n in pos_set:
                    continue

                pos_set.add(n)

                while data[n].isdigit():
                    s += data[n]
                    n += 1

                res += int(s)

    return res


def part2(data):
    row_len = data.find("\n") + 1
    res = 0
    for i in range(len(data)):
        if data[i] == "*":
            adj = adjacent_digits(data, i, row_len)
            if len(adj) < 2:
                continue
            poses = []
            nums = []
            for n in adj:
                s = ""
                while 0 <= n and data[n].isdigit():
                    n -= 1
                n += 1
                if n in poses:
                    continue

                poses.append(n)

                while data[n].isdigit():
                    s += data[n]
                    n += 1

                nums.append(int(s))
                if len(nums) > 2:
                    break

            if len(nums) == 2:
                res += nums[0] * nums[1]

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
