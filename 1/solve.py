from aocd import get_data, submit

DAY = 1
YEAR = 2023
data = get_data(day=DAY, year=YEAR)
# data = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"


def part1(l):
    res = 0
    for s in l:
        digits = [int(c) for c in s if c.isnumeric()]
        res += digits[0] * 10 + digits[-1]

    return res


def part2(l):
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

    return part1(new_l)


def main():
    p1 = part1(data.split("\n"))
    if p1:
        submit(p1, part="a", day=DAY, year=YEAR)
    p2 = part2(data.split("\n"))
    if p2:
        submit(p2, part="b", day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
