from aocd import get_data, submit

YEAR = 2025


def part1(data):
    l = data.split("\n")
    t=0
    for s in l:
        L = max(c for c in s[:-1])
        i = s.index(L)
        R = max(c for c in s[i+1:])
        t += int(L+R)
    return t


def part2(data):
    def largest(s, j):
        if j == 0:
            S = s
        else:
            S = s[:-j]
        L = max(c for c in S)
        i = s.index(L)
        return s[i+1:], L
    
    l = data.split("\n")
    t=0
    for s in l:
        T=""
        for i in range(11,-1,-1):
            s, d = largest(s,i)
            T+=d
        t+=int(T)
    return t


def main():
    day = int(__file__.split("/")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
