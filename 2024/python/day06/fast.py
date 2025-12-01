from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    pos = [0, 0]
    found = False
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] == "^":
                pos[0], pos[1] = y, x
                found = True
                break
        if found:
            break

    poses = set()
    poses.add(tuple(pos))
    dir_pos = 0
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while True:
        pos[0] += dirs[dir_pos][0]
        pos[1] += dirs[dir_pos][1]
        if not (0 <= pos[0] < len(l)) or not (0 <= pos[1] < len(l[0])):
            return len(poses)
        if l[pos[0]][pos[1]] == "#":
            pos[0] -= dirs[dir_pos][0]
            pos[1] -= dirs[dir_pos][1]
            dir_pos = (dir_pos - 1) % len(dirs)
            continue
        poses.add(tuple(pos))

def part2(data):
    l = data.split("\n")
    start_pos = [0, 0]
    found = False
    for y in range(len(l)):
        for x in range(len(l[0])):
            if l[y][x] == "^":
                start_pos[0], start_pos[1] = y, x
                found = True
                break
        if found:
            break

    poses = set()
    dir_pos = 0
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    pos = start_pos[::]
    while True:
        pos[0] += dirs[dir_pos][0]
        pos[1] += dirs[dir_pos][1]
        if not (0 <= pos[0] < len(l)) or not (0 <= pos[1] < len(l[0])):
            break
        if l[pos[0]][pos[1]] == "#":
            pos[0] -= dirs[dir_pos][0]
            pos[1] -= dirs[dir_pos][1]
            dir_pos = (dir_pos - 1) % len(dirs)
            pos[0] += dirs[dir_pos][0]
            pos[1] += dirs[dir_pos][1]
            if not (0 <= pos[0] < len(l)) or not (0 <= pos[1] < len(l[0])):
                break
        poses.add(tuple(pos))

    poses.discard(tuple(start_pos))
    t=0
    for block_pos in poses:
        loop_poses = set()
        dir_pos = 0
        loop_poses.add(tuple([*start_pos, dir_pos]))
        pos = start_pos[::]
        while True:
            pos[0] += dirs[dir_pos][0]
            pos[1] += dirs[dir_pos][1]
            if not (0 <= pos[0] < len(l)) or not (0 <= pos[1] < len(l[0])):
                break
            if (l[pos[0]][pos[1]] == "#") or (tuple(pos) == block_pos):
                pos[0] -= dirs[dir_pos][0]
                pos[1] -= dirs[dir_pos][1]
                dir_pos = (dir_pos - 1) % len(dirs)
                continue
            if tuple([*pos, dir_pos]) in loop_poses:
                t+=1
                break
            loop_poses.add(tuple([*pos, dir_pos]))
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
