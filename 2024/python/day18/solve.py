from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    blocks = set()
    for i in range(1024):
        s = l[i].split(",")
        blocks.add((int(s[1]), int(s[0])))
    
    SIZE = 70
    queue = [(0, 0, 0)]
    visited = set()
    while queue:
        y, x, weight = queue.pop(0)
        if not (0 <= y <= SIZE) or not (0 <= x <= SIZE) or (y, x) in blocks or (y, x) in visited:
            continue
        if (y, x) == (SIZE, SIZE):
            return weight

        
        visited.add((y, x))
        queue.append((y, x - 1, weight + 1))
        queue.append((y - 1, x, weight + 1))
        queue.append((y + 1, x, weight + 1))
        queue.append((y, x + 1, weight + 1))

def part2(data):
    l = data.split("\n")
    SIZE = 70
    blocks = set()
    i = 0
    while i < len(l):
        s = l[i].split(",")
        blocks.add((int(s[1]), int(s[0])))
    
        queue = [(0, 0, 0)]
        visited = set()
        while queue:
            y, x, weight = queue.pop(0)
            if not (0 <= y <= SIZE) or not (0 <= x <= SIZE) or (y, x) in blocks or (y, x) in visited:
                continue
            if (y, x) == (SIZE, SIZE):
                break
            
            visited.add((y, x))
            queue.append((y, x - 1, weight + 1))
            queue.append((y - 1, x, weight + 1))
            queue.append((y + 1, x, weight + 1))
            queue.append((y, x + 1, weight + 1))
        else:
            return l[i]
        i += 1


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
