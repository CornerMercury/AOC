from aocd import get_data, submit

YEAR = 2023


def part1(data):
    l = data.strip("\n").split(",")
    res = 0
    for part in l:
        cur = 0
        for c in part:
            cur += ord(c)
            cur *= 17
            cur %= 256
        res += cur

    return res


def hash(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur


def part2(data):
    l = data.strip("\n").split(",")
    boxes = {i: [] for i in range(256)}
    for part in l:
        if "=" in part:
            out = part.split("=")
            hash_num = hash(out[0])
            for i, lens in enumerate(boxes[hash_num]):
                if lens[0] == out[0]:
                    boxes[hash_num][i] = out
                    break
            else:
                boxes[hash_num].append(out)
        else:
            name = part[:-1]
            hash_num = hash(name)
            for i, lens in enumerate(boxes[hash_num]):
                if lens[0] == name:
                    boxes[hash_num].pop(i)
                    break
    res = 0
    for key, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            res += (key + 1) * (i + 1) * int(lens[1])
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
