from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./19i.txt")

    with open(path) as f:
        lines = [
            [robot.split() for robot in line.strip("\n").split(".")]
            for line in f.readlines()
        ]

    return [
        (
            (int(blueprint[0][6]), 0, 0),
            (int(blueprint[1][4]), 0, 0),
            (int(blueprint[2][4]), int(blueprint[2][7]), 0),
            (int(blueprint[3][4]), 0, int(blueprint[3][7])),
        )
        for blueprint in lines
    ]


def triangle_sum(n):
    return n * (n + 1) // 2


def bfs(blueprints, depth, start=((1, 0, 0), (0, 0, 0, 0))):
    to_visit = {start}
    max_geodes = 0
    max_ingredients = tuple(max(x) for x in zip(*blueprints))

    for i in range(1, depth):
        new_to_visit = set()
        max_geode_triangle = triangle_sum(depth - i)
        possible_max_geodes = max_geodes
        for node in to_visit:
            if max_geodes > max_geode_triangle + node[1][3]:
                continue

            blueprint = blueprints[0]
            if max_ingredients[0] != node[0][0] and all(
                x <= y for x, y in zip(blueprint, node[1])
            ):
                new_to_visit.add(
                    (
                        (node[0][0] + 1, node[0][1], node[0][2]),
                        (
                            node[1][0] - blueprint[0] + node[0][0],
                            node[1][1] - blueprint[1] + node[0][1],
                            node[1][2] - blueprint[2] + node[0][2],
                            node[1][3],
                        ),
                    )
                )

            blueprint = blueprints[1]
            if max_ingredients[1] != node[0][1] and all(
                x <= y for x, y in zip(blueprint, node[1])
            ):
                new_to_visit.add(
                    (
                        (node[0][0], node[0][1] + 1, node[0][2]),
                        (
                            node[1][0] - blueprint[0] + node[0][0],
                            node[1][1] - blueprint[1] + node[0][1],
                            node[1][2] - blueprint[2] + node[0][2],
                            node[1][3],
                        ),
                    )
                )

            blueprint = blueprints[2]
            if max_ingredients[2] != node[0][2] and all(
                x <= y for x, y in zip(blueprint, node[1])
            ):
                new_to_visit.add(
                    (
                        (node[0][0], node[0][1], node[0][2] + 1),
                        (
                            node[1][0] - blueprint[0] + node[0][0],
                            node[1][1] - blueprint[1] + node[0][1],
                            node[1][2] - blueprint[2] + node[0][2],
                            node[1][3],
                        ),
                    )
                )

            blueprint = blueprints[3]
            if all(x <= y for x, y in zip(blueprint, node[1])):
                new_to_visit.add(
                    (
                        node[0],
                        (
                            node[1][0] - blueprint[0] + node[0][0],
                            node[1][1] - blueprint[1] + node[0][1],
                            node[1][2] - blueprint[2] + node[0][2],
                            node[1][3] + (depth - i),
                        ),
                    )
                )
                possible_max_geodes = max(possible_max_geodes, node[1][3] + (depth - i))

            new_to_visit.add(
                (
                    node[0],
                    (
                        node[1][0] + node[0][0],
                        node[1][1] + node[0][1],
                        node[1][2] + node[0][2],
                        node[1][3],
                    ),
                )
            )

        to_visit = new_to_visit
        max_geodes = possible_max_geodes

    return max_geodes


def main():
    blueprints = get_data()
    total = 0
    for i, blueprint in enumerate(blueprints):
        total += (i + 1) * bfs(blueprint, 24)

    print(total)


if __name__ == "__main__":
    main()
