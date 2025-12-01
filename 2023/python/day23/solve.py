from aocd import get_data, submit
from collections import deque

YEAR = 2023


def part1(data):
    grid = [[c for c in line] for line in data.split("\n")]
    pos = complex(0, data.find("."))
    end = complex(len(grid) - 1, grid[-1].index("."))
    stack = deque([(set([pos]), pos)])
    max_path = 0
    while stack:
        pos_set, pos = stack.popleft()
        if pos == end:
            max_path = max(max_path, len(pos_set))
            continue
        dirs = [(1,), (-1j,), (-1,), (1j,), (1, 1j, -1, -1j)][
            "v<^>.".find(grid[int(pos.real)][int(pos.imag)])
        ]
        for d in dirs:
            new_pos = pos + d
            if not (0 <= new_pos.real < len(grid) and 0 <= new_pos.imag < len(grid[0])):
                continue
            if new_pos in pos_set:
                continue
            if grid[int(new_pos.real)][int(new_pos.imag)] != "#":
                stack.append((pos_set | set([new_pos]), new_pos))

    print(max_path - 1)
    return max_path - 1


def part2(data):
    grid = [[c for c in line] for line in data.split("\n")]
    start = complex(0, data.find("."))
    end = complex(len(grid) - 1, grid[-1].index("."))
    stack = deque([(start, start, start + 1, 1)])
    graph = {start: []}
    while stack:
        initial_pos, last_pos, pos, weight = stack.popleft()
        count = 0
        for d in (1, 1j, -1, -1j):
            new_pos = pos + d
            if not (0 <= new_pos.real < len(grid) and 0 <= new_pos.imag < len(grid[0])):
                continue
            if grid[int(new_pos.real)][int(new_pos.imag)] != "#":
                count += 1
        if count > 2 or new_pos.real == 0 or new_pos.real == len(grid) - 1:
            graph[initial_pos].append((pos, weight))
            initial_pos = pos
            weight = 0
            if pos not in graph:
                graph[pos] = []
            else:
                continue
        for d in (1, 1j, -1, -1j):
            new_pos = pos + d
            if new_pos == last_pos and pos not in graph:
                continue
            if not (0 <= new_pos.real < len(grid) and 0 <= new_pos.imag < len(grid[0])):
                continue
            if grid[int(new_pos.real)][int(new_pos.imag)] != "#":
                stack.append((initial_pos, pos, new_pos, weight + 1))

    max_path = 0
    stack = deque([(set([start]), start, 0)])
    while stack:
        visited, pos, weight = stack.popleft()
        if pos == end:
            max_path = max(max_path, weight)
            if max_path == weight:
                print(max_path)
            continue
        for node, next_weight in graph[pos]:
            if node in visited:
                continue
            stack.append((visited | set([node]), node, weight + next_weight))

    print(max_path)
    return max_path


data = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


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
