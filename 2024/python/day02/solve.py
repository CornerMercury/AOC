from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    t=0
    for s in l:
        i = *map(int, s.split()),
        t+=(max(abs(b-a) for a,b in zip(i, i[1:]))<=3)and(min(abs(b-a) for a,b in zip(i, i[1:]))>=1) and (([abs(b-a) for a,b in zip(i, i[1:])] == [b-a for a,b in zip(i, i[1:])])  or([abs(b-a) for a,b in zip(i, i[1:])] == [a-b for a,b in zip(i, i[1:])]))
    return t


def part2(data):
    l = data.split("\n")
    t=0
    for s in l:
        z = *map(int, s.split()),
        i=z[::]
        l=(max(abs(b-a) for a,b in zip(i, i[1:]))<=3)and(min(abs(b-a) for a,b in zip(i, i[1:]))>=1) and (([abs(b-a) for a,b in zip(i, i[1:])] == [b-a for a,b in zip(i, i[1:])])  or([abs(b-a) for a,b in zip(i, i[1:])] == [a-b for a,b in zip(i, i[1:])]))
        if l:
            t+=1
        else:
            for c in range(len(z)):
                i=z[:c] +z[c+1:]
                l=(max(abs(b-a) for a,b in zip(i, i[1:]))<=3)and(min(abs(b-a) for a,b in zip(i, i[1:]))>=1) and (([abs(b-a) for a,b in zip(i, i[1:])] == [b-a for a,b in zip(i, i[1:])])  or([abs(b-a) for a,b in zip(i, i[1:])] == [a-b for a,b in zip(i, i[1:])]))
                if l:
                    t+=1
                    b=True
                    break
                
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
