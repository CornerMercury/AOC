from aocd import get_data, submit

YEAR = 2025


def part1(data):
    l = data.split("\n")
    t=0
    for i,r in enumerate(l):
        for j,c in enumerate(r):
            rolls = 0
            if c != "@":
                continue
            for dr in range(-1,2):
                nr = i + dr
                if not (0 <= nr < len(l)):
                    continue 
                for dc in range(-1,2):
                    nc = j + dc
                    if not (0 <= nc < len(r)) or (dc == dr == 0):
                        continue
                    rolls += l[nr][nc] == "@"
            if rolls < 4:
                t+=1
    return t


def part2(data):
    l = data.split("\n")
    new_t = 0
    old_t = -1
    while old_t != new_t:
        old_t = new_t
        for i,r in enumerate(l):
            for j,c in enumerate(r):
                rolls = 0
                if c != "@":
                    continue
                for dr in range(-1,2):
                    nr = i + dr
                    if not (0 <= nr < len(l)):
                        continue 
                    for dc in range(-1,2):
                        nc = j + dc
                        if not (0 <= nc < len(r)) or (dc == dr == 0):
                            continue
                        rolls += l[nr][nc] == "@"
                if rolls < 4:
                    new_t += 1
                    l[i] = l[i][:j] + "." + l[i][j+1:]
    return new_t


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
