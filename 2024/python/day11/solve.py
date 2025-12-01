from aocd import get_data, submit
from functools import cache

YEAR=2024

def part1(data):
    l = data.strip().split(" ")
    for _ in range(25):
        i = 0
        while i < len(l):
            if l[i] == '0':
                l[i] = '1'
            elif len(l[i]) % 2 == 0:
                t = l[i]
                l[i] = str(int(t[:len(t)//2]))
                i+=1
                l.insert(i, str(int(t[len(t)//2:])))
            else:
                l[i] = str(int(l[i]) * 2024)
            i += 1
            
    return len(l)


def part2(data):
    l = data.strip().split(" ")
    @cache
    def split(stone, n):
        if n == 0:
            return 1
        if stone == 0:
            return split(1, n - 1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            return split(int(s[:len(s)//2]), n-1) + split(int(s[len(s)//2:]), n-1)
        else:
            return split(stone * 2024, n - 1)
    
    return sum(split(int(c), 75) for c in l)


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
