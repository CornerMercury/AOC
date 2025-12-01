from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    t = 0
    p = 16777216
    for s in l:
        s = int(s)
        for _ in range(2000):
            s ^= s * 64
            s %= p
            s ^= s // 32
            s %= p
            s ^= s * 2048
            s %= p
        t += s
    return t

def part2(data):
    l = data.split("\n")
    p = 16777216
    patterns = {}
    for s in l:
        s = int(s)
        r = [s % 10]
        cur_patterns = set()
        for i in range(2000):
            s ^= s * 64
            s %= p
            s ^= s // 32
            s %= p
            s ^= s * 2048
            s %= p
            r.append(s % 10)
            if i >= 4:
                t = (r[1] - r[0], r[2] - r[1], r[3] - r[2], r[4] - r[3])
                if t not in patterns:
                    patterns[t] = 0
                if t not in cur_patterns:
                    patterns[t] += r[4]
                    cur_patterns.add(t)
                r.pop(0)


    return max(patterns.values())


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
