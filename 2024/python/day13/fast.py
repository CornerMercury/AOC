from aocd import get_data, submit
import numpy as np

YEAR=2024

def part1(data):
    l = data.split("\n\n")
    t=0
    for claw in l:
        claw = claw.split('\n')
        c = claw[0].split(',')
        a = (int(c[0][-2:]), int(c[1][-2:]))
        c = claw[1].split(',')
        b = (int(c[0][-2:]), int(c[1][-2:]))
        c = claw[2].split(',')
        p = (int(c[0].split('=')[-1]), int(c[1].split('=')[-1]))
        
        A = np.array([[a[0], b[0]], [a[1], b[1]]])
        B = np.array([p[0], p[1]])
        C = list(np.linalg.solve(A,B))
        if np.allclose(C, np.round(C)):
            t += round(C[0])*3 + round(C[1])
    return t


def part2(data):
    l = data.split("\n\n")
    t=0
    for claw in l:
        claw = claw.split('\n')
        c = claw[0].split(',')
        a = (int(c[0][-2:]), int(c[1][-2:]))
        c = claw[1].split(',')
        b = (int(c[0][-2:]), int(c[1][-2:]))
        c = claw[2].split(',')
        p = (int(c[0].split('=')[-1]) + 10000000000000, int(c[1].split('=')[-1]) + 10000000000000)
        
        A = np.array([[a[0], b[0]], [a[1], b[1]]])
        B = np.array([p[0], p[1]])
        C = list(np.linalg.solve(A,B))
        C = (round(C[0]), round(C[1]))
        if (a[0]*C[0] + b[0]*C[1]) == p[0] and (a[1]*C[0] + b[1]*C[1]) == p[1]:
            t += round(C[0])*3 + round(C[1])
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
