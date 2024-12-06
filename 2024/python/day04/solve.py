from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    t=0
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] == 'X':
                try:
                    if ''.join(l[y][x+c] for c in range(0, 4)) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y][x-c] for c in range(0, 4)if x-c>=0) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y+c][x] for c in range(0, 4)) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y-c][x] for c in range(0, 4)if y-c>=0) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y-c][x-c] for c in range(0, 4)if (y-c>=0) and (x-c>=0)) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y-c][x+c] for c in range(0, 4)if y-c>=0) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y+c][x+c] for c in range(0, 4)) == 'XMAS':t+=1
                except:pass
                try:
                    if ''.join(l[y+c][x-c] for c in range(0, 4)if x-c>=0) == 'XMAS':t+=1
                except:pass
                
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
