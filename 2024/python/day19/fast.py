from aocd import get_data, submit
from functools import cache

YEAR=2024

def part1(data):
    available, possible = data.split("\n\n")
    available = available.split(', ')
    possible = possible.split("\n")
    t = 0
    for p in possible:
        stack = [0]
        while stack:
            index = stack.pop()
            if index == len(p):
                t += 1
                break
            for a in available:
                if p[index:].startswith(a):
                    stack.append(index + len(a))
    return t



def part2(data):
    available, possible = data.split("\n\n")
    available = available.split(', ')
    possible = possible.split("\n")
    t = 0
    
    @cache
    def count(p):
        if len(p) == 0:
            return 1
        s = 0
        for a in available:
            if p.startswith(a):
                s += count(p[len(a):])
        return s

    for p in possible:
        t += count(p)
    
    return t


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
