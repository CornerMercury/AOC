from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./19i.txt")

    with open(path) as f:
        lines = [[robot.split() for robot in line.strip('\n').split('.')] for line in f.readlines()]
    
    return [(
        (int(blueprint[3][4]), 0, int(blueprint[3][7])),
        (int(blueprint[2][4]), int(blueprint[2][7]), 0),
        (int(blueprint[1][4]), 0, 0),
        (int(blueprint[0][6]), 0, 0))
        for blueprint in lines
     ]

def triangle_sum(n):
    return n * (n + 1) // 2


def bfs(blueprints, depth, start=((0, 0, 0, 1), (0, 0, 0, 0))):
    to_visit = {start}
    max_geodes = 0

    for i in range(1, depth + 1):
        new_to_visit = set()
        max_geode_triangle = triangle_sum(depth - i)
        possible_max_geodes = max_geodes
        for node in to_visit:
            if max_geodes > max_geode_triangle + node[1][3]:
                continue

            possible_max_geodes = max(node[1][3] + node[0][0], possible_max_geodes)
            
            for j, blueprint in enumerate(blueprints):
                if all(x <= y for x, y in zip(blueprint, node[1])):
                    new_robots = list(node[0])
                    new_robots[j] += 1
                    new_to_visit.add((
                        tuple(new_robots),
                        (
                            node[1][0] - blueprint[0] + node[0][3],
                            node[1][1] - blueprint[1] + node[0][2],
                            node[1][2] - blueprint[2] + node[0][1],
                            node[1][3] + node[0][0]
                        )))

            new_to_visit.add((node[0], (
                            node[1][0] + node[0][3],
                            node[1][1] + node[0][2],
                            node[1][2] + node[0][1],
                            node[1][3] + node[0][0]
                        )))

        to_visit = new_to_visit
        max_geodes = possible_max_geodes

    print(max_geodes)
    return max_geodes





    


def main():
    blueprints = get_data()
    total = 0
    for i, blueprint in enumerate(blueprints):
        print(i+1)
        total += (i+1) * bfs(blueprint, 24)

    print(total)

if __name__ == '__main__':
    main()