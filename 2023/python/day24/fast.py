from aocd import get_data, submit
import numpy as np

YEAR = 2023


def part1(data):
    l = data.split("\n")
    hails = []
    for line in l:
        left, right = line.split(" @ ")
        pos = tuple(map(int, left.split(", ")))
        velocity = tuple(map(int, right.split(", ")))
        hails.append((pos, velocity))

    res = 0
    lower, upper = 200000000000000, 400000000000000
    for i, hail1 in enumerate(hails):
        for hail2 in hails[i + 1 :]:
            vx1 = hail1[1][0]
            vx2 = hail2[1][0]
            vy1 = hail1[1][1]
            vy2 = hail2[1][1]
            if vx2 * vy1 - vx1 * vy2 == 0:
                continue

            x1 = hail1[0][0]
            x2 = hail2[0][0]
            y1 = hail1[0][1]
            y2 = hail2[0][1]
            coefficients = np.array([[vx1, -vx2], [vy1, -vy2]])
            constants = np.array([x2 - x1, y2 - y1])
            s, t = np.linalg.solve(coefficients, constants)
            if s < 0 or t < 0:
                continue
            x = vx1 * s + x1
            y = vy1 * s + y1
            if lower <= x <= upper and lower <= y <= upper:
                res += 1
    return res


# cross product that takes in a vec and returns a cross with (x, y, z)^T
# each element is [x, y, z] coefficients
def variable_cross(vec):
    return [[0, vec[2], -vec[1]], [-vec[2], 0, vec[0]], [vec[1], -vec[0], 0]]


def part2(data):
    l = data.split("\n")
    hails = []
    for line in l:
        left, right = line.split(" @ ")
        pos = tuple(map(int, left.split(", ")))
        velocity = tuple(map(int, right.split(", ")))
        hails.append((pos, velocity))

    coefficients = []
    constants = []
    m = [[0, 0, 0, 1, 0, -1], [0, -1, 0, 0, 1, 0], [1, 0, -1, 0, 0, 0]]
    for pv, vv in hails[3:7]:
        constants += list(np.cross(pv, vv))
        # x, y, z, X, Y, Z, xY, xZ, yX, yZ, zX, zY
        final = [[], [], []]
        p = variable_cross(pv)
        v = variable_cross(vv)
        for i, row in enumerate(final):
            row.extend(p[i])
            row.extend(v[i])
            row.extend(m[i])
        coefficients += final

    print(coefficients)
    out = list(np.linalg.solve(np.array(coefficients), np.array(constants)))
    res = sum(out[3:6])
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
