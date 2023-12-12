from aocd import get_data, submit
from itertools import product
from functools import lru_cache

YEAR = 2023


def get_line(s):
    c = 0
    out = []
    for i in range(len(s)):
        if s[i] == "#":
            c += 1
        else:
            if c != 0:
                out.append(c)
                c = 0
    if c != 0:
        out.append(c)

    return out


def part1(data):
    l = data.split("\n")
    res = 0
    for line in l:
        line, int_lst = line.split()
        int_lst = list(map(int, int_lst.split(",")))
        q_count = line.count("?")
        for tup in product(".#", repeat=q_count):
            new_line = line
            for c in tup:
                new_line = new_line.replace("?", c, 1)
            if get_line(new_line) == int_lst:
                res += 1
    return res


@lru_cache(maxsize=None)
def rec(s, cur_count, cur_lst, target_lst):
    if not s:
        if cur_count != 0:
            cur_lst += (cur_count,)
        return cur_lst == target_lst

    if len(cur_lst) > len(target_lst):
        return 0
    if cur_lst and cur_lst[-1] != target_lst[len(cur_lst) - 1]:
        return 0
    if s[0] == "?":
        return rec("#" + s[1:], cur_count, cur_lst, target_lst) + rec(
            "." + s[1:], cur_count, cur_lst, target_lst
        )
    if s[0] == "#":
        return rec(s[1:], cur_count + 1, cur_lst, target_lst)
    if s[0] == ".":
        if cur_count != 0:
            cur_lst += (cur_count,)
        return rec(s[1:], 0, cur_lst, target_lst)


def part2(data):
    res = 0
    l = data.split("\n")
    for line in l:
        line, int_lst = line.split()
        int_lst = list(map(int, int_lst.split(",")))
        res += rec("?".join([line] * 5), 0, tuple(), tuple(int_lst * 5))

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
