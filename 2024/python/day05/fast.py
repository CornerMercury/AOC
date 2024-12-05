from aocd import get_data, submit
from functools import cmp_to_key

YEAR = 2024

def part1(data):
    l = data.split("\n")
    o = {}
    i=0
    while l[i]!='':
        a,b = l[i].split("|")
        if a not in o:
            o[a]=set()
        o[a].add(b)
        i+=1
    t=0
    for s in l[i+1:]:
        ns = s.split(',')
        c=True
        for i in range(len(ns)):
            for j in range(0, i):
                if (ns[i] in o) and (ns[j] in o[ns[i]]):
                    c = False
                    break
            if not c:
                break
        else:
            t+=int(ns[len(ns)//2])
    return t


def part2(data):
    l = data.split("\n")
    rules = {}
    i=0
    while l[i]!='':
        a,b = l[i].split("|")
        a,b = int(a), int(b)
        if a not in rules:
            rules[a]=set()
        rules[a].add(b)
        i+=1
    t=0
    for s in l[i+1:]:
        pages = list(map(int, s.split(',')))
        i=0
        new_pages = sorted(pages,key=cmp_to_key(lambda a,b: 1 if a in rules[b] else -1))
        if pages != new_pages:
            t+=new_pages[len(pages)//2]
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
