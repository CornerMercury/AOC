from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    t=0
    for y in range(len(l)-4):
        for x in range(len(l[0])-4):
            if l[y][x] == 'X':
                if (l[y+1][x+1] == "M") and (l[y+2][x+2] == "A") and (l[y+3][x+3] == "S"):t+=1
                if (l[y+1][x] == "M") and (l[y+2][x] == "A") and (l[y+3][x] == "S"):t+=1
                if (l[y][x+1] == "M") and (l[y][x+2] == "A") and (l[y][x+3] == "S"):t+=1
            if l[y][x] == 'S':
                if (l[y+1][x+1] == "A") and (l[y+2][x+2] == "M") and (l[y+3][x+3] == "X"):t+=1
                if (l[y+1][x] == "A") and (l[y+2][x] == "M") and (l[y+3][x] == "X"):t+=1
                if (l[y][x+1] == "A") and (l[y][x+2] == "M") and (l[y][x+3] == "X"):t+=1
            if (l[y][x+3] == "X") and (l[y+1][x+2] == "M") and (l[y+2][x+1] == "A") and (l[y+3][x] == "S"):t+=1
            if (l[y][x+3] == "S") and (l[y+1][x+2] == "A") and (l[y+2][x+1] == "M") and (l[y+3][x] == "X"):t+=1
                
    return t

def part2(data):
    l = data.split("\n")
    t=0
    for y in range(1,len(l)-1):
        for x in range(1,len(l[0])-1):
            if l[y][x] == 'A':
                a=l[y-1][x-1]
                b,c=l[y+1][x-1],l[y-1][x+1]
                d=l[y+1][x+1]
                if ((a==b and c==d) or (a==c and b==d)) and sorted(a+d)==['M','S']:
                    t+=1
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
