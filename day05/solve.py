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


# def part2(data):
#     l = [s.split(":")[1].split("\n") for s in data.split("\n\n")]
#     seeds, l = list(map(int, l[0][0].split())), l[1:][::-1]
#     l = [[list(map(int, line.split())) for line in mapping[1:]] for mapping in l]

#     loc = 0
#     while True:
#         loc += 1
#         last = loc
#         for mapping in l:
#             for dest, source, rang in mapping:
#                 if dest <= last < dest + rang:
#                     new_last = last - dest + source
#                     break
#                 else:
#                     new_last = last
#             last = new_last
#         for i in range(0, len(seeds), 2):
#             if seeds[i] <= last < seeds[i] + seeds[i + 1]:
#                 return loc


def part2(data):
    l = [s.split(":")[1].split("\n") for s in data.split("\n\n")]
    seeds, l = list(map(int, l[0][0].split())), l[1:][::-1]
    l = [[list(map(int, line.split())) for line in mapping[1:]] for mapping in l]
    seed_pairs = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    min_loc = 999999999999
    for pair in seed_pairs:
        stack = [pair]
        next_stack = []
        # bfs
        for mapping in l:
            while stack:
                node = stack.pop()
                for dest, source, rang in mapping:
                    end = dest + rang
                    # ranges do not overlap 01() or ()01
                    if node[1] < source or node[0] >= end:
                        continue
                    # 0(1)
                    elif node[0] < source and node[1] < end:
                        next_stack.append((dest, dest + node[1] - source))
                        stack.append((node[0], source - 1))
                        break
                    # (01)
                    elif source <= node[0] <= node[1] < end:
                        next_stack.append(
                            (dest + node[0] - source, dest + node[1] - source)
                        )
                        break
                    # (0)1
                    elif node[0] < source and end <= node[1]:
                        next_stack.append((dest + node[0] - source, end - 1))
                        stack.append((source + range, node[1]))
                        break
                    # 0()1
                    elif node[0] < source and end <= node[1]:
                        stack.append((node[0], source - 1))
                        next_stack.append((dest, end - 1))
                        stack.append((end, node[1]))
                        break
                else:
                    next_stack.append(node)

            stack = next_stack
            next_stack = []
        min_loc = min(min_loc, min(map(lambda x: x[0], stack)))

    print(min_loc)
    return None


data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def main():
    day = int(__file__.split("\\")[-2][-2:])
    # data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
