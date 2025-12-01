from aocd import get_data, submit


YEAR = 2023


def part1(data):
    l = [s.split(":")[1].split("\n") for s in data.split("\n\n")]
    last, l = map(int, l[0][0].split()), l[1:]
    for mapping in l:
        new_last = []
        for n in last:
            for line in mapping[1:]:
                dest, source, rang = map(int, line.split())
                if source <= n < source + rang:
                    new_last.append(n - source + dest)
                    break
            else:
                new_last.append(n)

        last = new_last

    return min(last)


def part2(data):
    l = [s.split(":")[1].split("\n") for s in data.split("\n\n")]
    seeds, l = list(map(int, l[0][0].split())), l[1:]
    l = [[list(map(int, line.split())) for line in mapping[1:]] for mapping in l]
    stack = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    next_stack = []
    # bfs
    for mapping in l:
        while stack:
            node = stack.pop()
            for dest, source, rang in mapping:
                end = dest + rang
                source_end = source + rang
                # ranges do not overlap 01() or ()01
                if node[1] < source or node[0] >= source_end:
                    continue
                # (01)
                elif source <= node[0] and node[1] < source_end:
                    next_stack.append(
                        (dest + node[0] - source, dest + node[1] - source)
                    )
                    break
                # 0(1)
                elif node[0] < source and node[1] < source_end:
                    next_stack.append((dest, dest + node[1] - source))
                    stack.append((node[0], source - 1))
                    break
                # (0)1
                elif source <= node[0] and source_end <= node[1]:
                    next_stack.append((dest + node[0] - source, end - 1))
                    stack.append((source_end, node[1]))
                    break
                # 0()1
                elif node[0] < source and source_end <= node[1]:
                    stack.append((node[0], source - 1))
                    next_stack.append((dest, end - 1))
                    stack.append((source_end, node[1]))
                    break
            else:
                next_stack.append(node)

        stack = next_stack
        next_stack = []

    return min(map(lambda x: x[0], stack))


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
