from aocd import get_data, submit
from functools import cache

YEAR = 2025

@cache
def point_in_area(y, x):
    n = len(nodes)
    for i in range(n+1):
        y_1, x_1 = nodes[i%n]
        y_2, x_2 = nodes[(i+1)%n]

        if y_1 == y_2:
            if y == y_1 and min(x_1, x_2) <= x <= max(x_1, x_2):
                return True

        if x_1 == x_2:
            if x == x_1 and min(y_1, y_2) <= y <= max(y_1, y_2):
                return True
    inside = False
    for i in range(n):
        y_1, x_1 = nodes[i%n]
        y_2, x_2 = nodes[(i+1)%n]
        if x > min(x_1, x_2) and x <= max(x_1, x_2):
            if y <= max(y_1, y_2):
                if x_1 != x_2:
                    xinters = (x - x_1) * (y_2 - y_1) / (x_2 - x_1) + y_1
                if y_1 == y_2 or y <= xinters:
                    inside = not inside
    
    return inside


def part1(data):
    l = data.split("\n")
    nodes = [(int(a),int(b)) for a,b in map(lambda x: x.split(","), l)]
    max_area = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            left = nodes[i]
            right = nodes[j]
            max_area = max(max_area, (abs(left[0] - right[0]) + 1)*(abs(left[1] - right[1]) + 1))

    print(max_area)
    return max_area


nodes = []
def part2(data):
    l = data.split("\n")
    global nodes
    nodes = [(int(a),int(b)) for a,b in map(lambda x: x.split(","), l)]
    n = len(nodes)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            y_1, x_1 = nodes[i]
            y_2, x_2 = nodes[j]
            area = (abs(y_1 - y_2) + 1)*(abs(x_1 - x_2) + 1)
            if area <= max_area:
                continue
            y = min(y_1, y_2)
            if not all(point_in_area(y, x) for x in range(min(x_1, x_2), max(x_1, x_2) + 1)):
                continue
            y = max(y_1, y_2)
            if not all(point_in_area(y, x) for x in range(min(x_1, x_2), max(x_1, x_2) + 1)):
                continue
            x = min(x_1, x_2)
            if not all(point_in_area(y, x) for y in range(min(y_1, y_2) + 1, max(y_1, y_2))):
                continue
            x = max(x_1, x_2)
            if not all(point_in_area(y, x) for y in range(min(y_1, y_2) + 1, max(y_1, y_2))):
                continue
            max_area = area

    return max_area


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
