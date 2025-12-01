from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    WIDTH = 101
    HEIGHT = 103
    robots = []
    for s in l:
        p, v = s.split()
        p = p.split("=")[1]
        x, y = map(int, p.split(","))
        v = v.split("=")[1]
        dx, dy = map(int, v.split(","))
        robots += [([y, x], (dy, dx))]
    
    for _ in range(100):
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % HEIGHT
            robot[0][1] = (robot[0][1] + robot[1][1]) % WIDTH

    quads = [0, 0, 0, 0]
    for pos, _ in robots:
        y, x = pos
        if 0 <= y < HEIGHT // 2:
            if 0 <= x < WIDTH // 2:
                quads[0] += 1
            elif (WIDTH - (WIDTH // 2)) <= x < WIDTH:
                quads[1] += 1
        elif (HEIGHT - (HEIGHT // 2)) <= y < HEIGHT:
            if 0 <= x < WIDTH // 2:
                quads[2] += 1
            elif (WIDTH - (WIDTH // 2)) <= x < WIDTH:
                quads[3] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


def part2(data):
    l = data.split("\n")
    WIDTH = 101
    HEIGHT = 103
    robots = []
    for s in l:
        p, v = s.split()
        p = p.split("=")[1]
        x, y = map(int, p.split(","))
        v = v.split("=")[1]
        dx, dy = map(int, v.split(","))
        robots += [([y, x], (dy, dx))]
    
    i = 1
    while True:
        poses = {}
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % HEIGHT
            robot[0][1] = (robot[0][1] + robot[1][1]) % WIDTH
            poses[tuple(robot[0])] = poses.get(tuple(robot[0]), 0) + 1
        
        t = 0
        for pos, size in poses.items():
            y, x = pos
            if (y + 1 < HEIGHT and (y + 1, x) in poses) + (
                    0 <= y - 1 and (y - 1, x) in poses) + (
                x + 1 < WIDTH and (y, x + 1) in poses) +  (
                    0 <= x - 1 and (y, x - 1) in poses) >= 3:
                t += size
        if len(robots) * 0.3 < t:
            return i
        
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
