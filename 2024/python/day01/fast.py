from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    a=[]
    b=[]
    for s in l:
        c,d = s.split()
        a+=[int(c)]
        b+=[int(d)]
    
    return sum(abs(c-d) for c,d in zip(sorted(a),sorted(b)))


def part2(data):
    l = data.split("\n")
    a=[]
    b=[]
    for s in l:
        c,d = s.split()
        a+=[int(c)]
        b+=[int(d)]

    t=0
    for c in a:
        t+=c*b.count(c)
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
