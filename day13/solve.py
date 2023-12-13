from aocd import get_data, submit

YEAR = 2023


def part1(data):
    data += "\n"
    l = data.split("\n")
    square = []
    res = 0
    for line in l:
        if line != "":
            square.append([c for c in line])
            continue
        for y in range(1, len(square)):
            ny = y - 1
            py = y
            while 0 <= ny and py < len(square):
                if not all(
                    square[ny][x] == square[py][x] for x in range(len(square[0]))
                ):
                    break
                ny -= 1
                py += 1
            else:
                res += y * 100
                break
        for x in range(1, len(square[0])):
            nx = x - 1
            px = x
            while 0 <= nx and px < len(square[0]):
                if not all(square[y][nx] == square[y][px] for y in range(len(square))):
                    break
                nx -= 1
                px += 1
            else:
                res += x
                break
        square = []
    return res


def get_hori(square, ogy=-1):
    for y in range(1, len(square)):
        ny = y - 1
        py = y
        while 0 <= ny and py < len(square):
            if not all(square[ny][x] == square[py][x] for x in range(len(square[0]))):
                break
            ny -= 1
            py += 1
        else:
            if ogy != y:
                return y
    return -1


def get_vert(square, ogx=-1):
    for x in range(1, len(square[0])):
        nx = x - 1
        px = x
        while 0 <= nx and px < len(square[0]):
            if not all(square[y][nx] == square[y][px] for y in range(len(square))):
                break
            nx -= 1
            px += 1
        else:
            if ogx != x:
                return x
    return -1


def p2_helper(square):
    og = get_hori(square), get_vert(square)
    for ly in range(len(square)):
        for lx in range(len(square[0])):
            square[ly][lx] = "." if square[ly][lx] == "#" else "#"
            new = (get_hori(square, ogy=og[0]), get_vert(square, ogx=og[1]))
            if new != (-1, -1):
                if new[0] != -1:
                    return new[0] * 100
                elif new[1] != -1:
                    return new[1]
            square[ly][lx] = "." if square[ly][lx] == "#" else "#"


def part2(data):
    data += "\n"
    l = data.split("\n")
    square = []
    res = 0
    for line in l:
        if line != "":
            square.append([c for c in line])
            continue
        res += p2_helper(square)
        square = []
    return res


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
