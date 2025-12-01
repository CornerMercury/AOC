from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    for y, row in enumerate(l):
        for x, c in enumerate(row):
            if c == 'S':
                start_pos = (y, x)

    queue = [(start_pos[0], start_pos[1], 0)]
    weights = [[-1] * len(l[0]) for _ in range(len(l))]
    while queue:
        y, x, w = queue.pop(0)
        if not (0 <= y < len(l)) or not (0 <= x < len(l[0])) or (l[y][x] == '#') or (weights[y][x] != -1):
            continue
        
        weights[y][x] = w

        queue.append((y + 1, x, w + 1))
        queue.append((y, x + 1, w + 1))
        queue.append((y - 1, x, w + 1))
        queue.append((y, x - 1, w + 1))
    
    t = 0
    for y in range(1, len(l) - 1):
        for x in range(1, len(l[0]) - 1):
            if weights[y][x] == -1:
                continue
            if y + 2 < len(l) and weights[y + 2][x] != -1 and abs(weights[y][x] - weights[y + 2][x]) - 1 >= 100:
                t += 1
            if x + 2 < len(l[0]) and weights[y][x + 2] != -1 and abs(weights[y][x] - weights[y][x + 2]) - 1 >= 100:
                t += 1
    return t

            

def part2(data):
    l = data.split("\n")
    for y, row in enumerate(l):
        for x, c in enumerate(row):
            if c == 'S':
                start_pos = (y, x)

    queue = [(start_pos[0], start_pos[1], 0)]
    weights = {}
    while queue:
        y, x, w = queue.pop(0)
        if not (0 <= y < len(l)) or not (0 <= x < len(l[0])) or (l[y][x] == '#') or ((y, x) in weights):
            continue
        
        weights[(y, x)] = w

        queue.append((y + 1, x, w + 1))
        queue.append((y, x + 1, w + 1))
        queue.append((y - 1, x, w + 1))
        queue.append((y, x - 1, w + 1))
    
    t = 0
    MAX_DISTANCE = 20
    for y in range(1, len(l)-1):
        for x in range(1, len(l[0])-1):
            if (y, x) not in weights:
                continue
            for dy in range(0, MAX_DISTANCE + 1):
                for dx in range(-MAX_DISTANCE + abs(dy), MAX_DISTANCE - abs(dy) + 1):
                    if (y + dy, x + dx) not in weights or (dy == 0 and dx >= 0):
                        continue
                    if abs(weights[(y, x)] - weights[(y + dy, x + dx)]) - abs(dy) - abs(dx) >= 100:
                        t += 1

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
