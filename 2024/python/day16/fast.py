from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(len(l) - 2, 1, 1, 0)]
    weights = {}
    min_cost = 9999999999999999
    while stack:
        y, x, dir_pos, weight = stack.pop()
        if weight >= min_cost:
            continue
        
        if (y, x, dir_pos) not in weights or weights[(y, x, dir_pos)] > weight:
            weights[(y, x, dir_pos)] = weight
            if l[y][x] == 'E':
                min_cost = weight
                continue
        else:
            continue
        
        left = dirs[(dir_pos + 1) % 4]
        right = dirs[(dir_pos - 1) % 4]
        straight = dirs[dir_pos]
        if l[y + straight[0]][x + straight[1]] != "#":
            stack.append((y + straight[0], x + straight[1], dir_pos, weight + 1))
        if l[y + left[0]][x + left[1]] != "#":
            stack.append((y + left[0], x + left[1], (dir_pos + 1) % 4, weight + 1001))
        if l[y + right[0]][x + right[1]] != "#":
            stack.append((y + right[0], x + right[1], (dir_pos - 1) % 4, weight + 1001))

    return min_cost


def part2(data):
    l = data.split("\n")
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [(len(l) - 2, 1, 1, 0, [])]
    weights = {}
    min_cost = part1(data)
    tiles = set()
    while stack:
        y, x, dir_pos, weight, path = stack.pop()
        if weight > min_cost:
            continue
        
        path = path[::] + [(y, x)]
        if (y, x, dir_pos) not in weights or weights[(y, x, dir_pos)] > weight:
            weights[(y, x, dir_pos)] = weight
            if l[y][x] == 'E':
                min_cost = weight
                tiles = set(path)
                continue
        elif (weights[(y, x, dir_pos)] == weight) and (y, x) in tiles:
            tiles |= set(path)
            continue
        else:
            continue
        
        left = dirs[(dir_pos + 1) % 4]
        right = dirs[(dir_pos - 1) % 4]
        straight = dirs[dir_pos]
        if l[y + straight[0]][x + straight[1]] != "#":
            stack.append((y + straight[0], x + straight[1], dir_pos, weight + 1 , path))
        if l[y + left[0]][x + left[1]] != "#":
            stack.append((y, x, (dir_pos + 1) % 4, weight + 1000, path))
        if l[y + right[0]][x + right[1]] != "#":
            stack.append((y, x, (dir_pos - 1) % 4, weight + 1000, path))

    return len(tiles)


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
