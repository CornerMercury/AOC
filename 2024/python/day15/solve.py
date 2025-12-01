from aocd import get_data, submit

YEAR=2024

def part1(data):
    m, moves = data.split("\n\n")
    m = m.split("\n")
    pos = [0, 0]
    for y, row in enumerate(m):
        for x, c in enumerate(m[y]):
            if c == '@':
                pos = [y, x]
                break

    m = [[c if c != '@' else '.' for c in m[i]] for i in range(len(m))]
    for move in moves.replace('\n', ''):
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]["v>^<".index(move)]
        new_pos = pos[::]
        new_pos[0] += dir[0]
        new_pos[1] += dir[1]
        new_char = m[new_pos[0]][new_pos[1]]
        if new_char == '.':
            pos = new_pos
            continue
        if new_char == '#':
            continue
        
        box_pos = new_pos[::]
        while m[box_pos[0]][box_pos[1]] == 'O':
            box_pos[0] += dir[0]
            box_pos[1] += dir[1]

        new_char = m[box_pos[0]][box_pos[1]]
        if new_char == '#':
            continue
        
        m[box_pos[0]][box_pos[1]] = 'O'
        m[new_pos[0]][new_pos[1]] = '.'
        pos = new_pos[::]

    t = 0
    for y, row in enumerate(m):
        for x, c in enumerate(m[y]):
            if c == 'O':
                t += 100 * y + x
    return t


def part2(data):
    mu, moves = data.split("\n\n")
    mu = mu.split("\n")
    pos = [0, 0]
    for y, row in enumerate(mu):
        for x, c in enumerate(mu[y]):
            if c == '@':
                pos = [y, x * 2]
                break
    
    m=[]
    for i in range(len(mu)):
        r=[]
        for c in mu[i]:
            if c == 'O':
                r.append('[')
                r.append(']')
                continue
            if c == '@':
                c = '.'
            r.append(c)
            r.append(c)
        m.append(r)

    def r(pos, dir):
        if m[pos[0]][pos[1]] == '.':
            return True
        if m[pos[0]][pos[1]] == '[':
            return r([pos[0] + dir[0], pos[1] + dir[1]], dir) and r([pos[0] + dir[0], pos[1] + dir[1] + 1], dir)
        return 


    for move in moves.replace('\n', ''):
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]["v>^<".index(move)]
        new_pos = pos[::]
        new_pos[0] += dir[0]
        new_pos[1] += dir[1]
        new_char = m[new_pos[0]][new_pos[1]]
        if new_char == '.':
            pos = new_pos
            continue
        if new_char == '#':
            continue
        
        box_pos = new_pos[::]
        while m[box_pos[0]][box_pos[1]] == 'O':
            box_pos[0] += dir[0]
            box_pos[1] += dir[1]

        new_char = m[box_pos[0]][box_pos[1]]
        if new_char == '#':
            continue
        
        m[box_pos[0]][box_pos[1]] = 'O'
        m[new_pos[0]][new_pos[1]] = '.'
        pos = new_pos[::]

    t = 0
    for y, row in enumerate(m):
        for x, c in enumerate(m[y]):
            if c == 'O':
                t += 100 * y + x
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
