from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    t = 0
    seen = set()
    for y in range(len(l)):
        for x in range(len(l[0])):
            if (y, x) in seen:
                continue
            c = l[y][x]
            area = 0
            perim = 0
            stack = [(y, x)]
            while stack:
                a, b = stack.pop()
                if ((a, b) in seen) and (l[a][b] == c):
                    continue
                if not (0 <= a < len(l)) or not (0 <= b < len(l[0])) or (l[a][b] != c) :
                    perim += 1
                    continue
                seen.add((a, b))
                area += 1
                stack.append((a + 1, b))
                stack.append((a - 1, b))
                stack.append((a, b + 1))
                stack.append((a, b - 1))
            t += area * perim
    return t


def part2(data):
    l = data.split("\n")
    t = 0
    seen = set()
    for y in range(len(l)):
        for x in range(len(l[0])):
            if (y, x) in seen:
                continue
            c = l[y][x]
            area = 0
            n_sides = 0
            stack = [(y, x)]
            while stack:
                a, b = stack.pop()
                if ((a, b) in seen) and (l[a][b] == c):
                    continue
                if not (0 <= a < len(l)) or not (0 <= b < len(l[0])) or (l[a][b] != c) :
                    continue
                seen.add((a, b))
                area += 1
                for dy, dx in ((1, -1), (1, 1), (-1, 1), (-1, -1)):
                    if (not (0 <= a < len(l)) or not (0 <= b + dx < len(l[0])) or (l[a][b + dx] != c)) and (
                        not (0 <= a + dy < len(l)) or not (0 <= b < len(l[0])) or (l[a + dy][b] != c)):
                        n_sides += 1
                    if ((0 <= a < len(l)) and (0 <= b + dx < len(l[0])) and (l[a][b + dx] == c)) and (
                        (0 <= a + dy < len(l)) and (0 <= b < len(l[0])) and (l[a + dy][b] == c)) and (
                        l[a + dy][b + dx] != c):
                        n_sides += 1
                stack.append((a + 1, b))
                stack.append((a - 1, b))
                stack.append((a, b + 1))
                stack.append((a, b - 1))
            
            t += area * n_sides
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
