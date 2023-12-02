from aocd import get_data, submit, get_day_and_year

YEAR = 2023


def part1(data):
    l = data.split("\n")
    res = 0
    for s in l:
        digits = [int(c) for c in s if c.isnumeric()]
        res += digits[0] * 10 + digits[-1]

    return res


def part2(data):
    l = data.split("\n")
    word_list = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    new_l = []
    for s in l:
        for i in range(len(word_list)):
            w = word_list[i]
            s = s.replace(w, w + str(i + 1) + w)
        new_l.append(s)

    return part1("\n".join(new_l))


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
