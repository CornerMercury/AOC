from aocd import get_data, submit

YEAR=2024

def part1(data):
    t=0
    l=data
    for i in range(len(l)):
        if l[i:i+4] == 'mul(':
            p=j=i+4
            while l[j].isnumeric():
                j+=1
            if l[j]!=',':
                continue
            a=int(l[p:j])
            p=j=j+1
            while l[j].isnumeric():
                j+=1
            if l[j]!=')':
                continue
            t+=a*int(l[p:j])
    return t


def part2(data):
    t=0
    l=data
    on=True
    for i in range(len(l)):
        if on:
            if l[i:i+4] == 'mul(':
                p=j=i+4
                while l[j].isnumeric():
                    j+=1
                if l[j]!=',':
                    continue
                a=int(l[p:j])
                p=j=j+1
                while l[j].isnumeric():
                    j+=1
                if l[j]!=')':
                    continue
                t+=a*int(l[p:j])
            elif l[i:i+7] == 'don\'t()':
                on=False
        else:
            if l[i:i+4] == 'do()':
                on=True
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
