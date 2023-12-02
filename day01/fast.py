from aocd import get_data, submit
from collections import deque

YEAR = 2023


def part1(data):
    l = data.split("\n")
    res = 0
    for s in l:
        for i in range(0, len(s)):
            if s[i].isdigit():
                res += int(s[i]) * 10
            else:
                break

        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                res += int(s[i])
            else:
                break

    return res


def part2(data):
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
    for i in range(len(word_list)):
        w = word_list[i]
        data = data.replace(w, w + str(i + 1) + w)

    return part1(data)


def main():
    day = int(__file__.split("\\")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    for _ in range(20):
        p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
