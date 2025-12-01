from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./19i.txt")

    with open(path) as f:
        lines = [[robot.split() for robot in line.strip('\n').split('.')] for line in f.readlines()]
    
    return [(
        (int(blueprint[0][6]), 0, 0),
        (int(blueprint[1][4]), 0, 0),
        (int(blueprint[2][4]), int(blueprint[2][7]), 0),
        (int(blueprint[3][4]), 0, int(blueprint[3][7]))
        )
        for blueprint in lines
     ]

def triangle_sum(n):
    return n * (n + 1) // 2

def dfs(node, blueprints, max_ing, visited=set(), max_geodes=0):
    if node not in visited:
        if node[2] <= 0:
            return max_geodes

        visited.add(node)
        if max_geodes > triangle_sum(node[2]) + node[2]:
            return max_geodes

        #Geode
        blueprint = blueprints[3]
        t_node = node
        while t_node[2] >= 1 and all(x <= y for x, y in zip(blueprint, t_node[1])) == False:
            t_node = (
                            t_node[0],
                            (
                                t_node[1][0] + t_node[0][0],
                                t_node[1][1] + t_node[0][1],
                                t_node[1][2] + t_node[0][2],
                                t_node[1][3]
                            ),
                            t_node[2] - 1
                        )
        if t_node[2] >= 1:
            t_node = (
                            t_node[0],
                            (
                            t_node[1][0] - blueprint[0] + t_node[0][0],
                            t_node[1][1] - blueprint[1] + t_node[0][1],
                            t_node[1][2] - blueprint[2] + t_node[0][2],
                            t_node[1][3] + t_node[2]
                            ),
                            t_node[2] - 1
                        )

            if max_geodes < t_node[1][3] + t_node[2]:
                print(t_node)
            max_geodes = dfs(t_node, blueprints, max_ing, visited, max(max_geodes, t_node[1][3] + t_node[2]))

        #Obsidian
        if max_ing[2] != node[0][2]:
            blueprint = blueprints[2]
            t_node = node
            while t_node[2] >= 1 and all(x <= y for x, y in zip(blueprint, t_node[1])) == False:
                t_node = (
                                t_node[0],
                                (
                                    t_node[1][0] + t_node[0][0],
                                    t_node[1][1] + t_node[0][1],
                                    t_node[1][2] + t_node[0][2],
                                    t_node[1][3]
                                ),
                                t_node[2] - 1
                            )
            if t_node[2] >= 1:
                t_node = (
                                (
                                t_node[0][0],
                                t_node[0][1],
                                t_node[0][2] + 1
                                ),
                                (
                                t_node[1][0] - blueprint[0] + t_node[0][0],
                                t_node[1][1] - blueprint[1] + t_node[0][1],
                                t_node[1][2] - blueprint[2] + t_node[0][2],
                                t_node[1][3]
                                ),
                                t_node[2] - 1
                            )
                            
                max_geodes = dfs(t_node, blueprints, max_ing, visited, max_geodes)

        #Clay
        if max_ing[1] != node[0][1]:
            blueprint = blueprints[1]
            t_node = node
            while t_node[2] >= 1 and all(x <= y for x, y in zip(blueprint, t_node[1])) == False:
                t_node = (
                                t_node[0],
                                (
                                    t_node[1][0] + t_node[0][0],
                                    t_node[1][1] + t_node[0][1],
                                    t_node[1][2] + t_node[0][2],
                                    t_node[1][3]
                                ),
                                t_node[2] - 1
                            )
            if t_node[2] >= 1:
                t_node = (
                                (
                                t_node[0][0],
                                t_node[0][1] + 1,
                                t_node[0][2]
                                ),
                                (
                                t_node[1][0] - blueprint[0] + t_node[0][0],
                                t_node[1][1] - blueprint[1] + t_node[0][1],
                                t_node[1][2] - blueprint[2] + t_node[0][2],
                                t_node[1][3]
                                ),
                                t_node[2] - 1
                            )
                            
                max_geodes = dfs(t_node, blueprints, max_ing, visited, max_geodes)

        #Ore
        if max_ing[0] != node[0][0]:
            blueprint = blueprints[0]
            t_node = node
            while t_node[2] >= 1 and all(x <= y for x, y in zip(blueprint, t_node[1])) == False:
                t_node = (
                                t_node[0],
                                (
                                    t_node[1][0] + t_node[0][0],
                                    t_node[1][1] + t_node[0][1],
                                    t_node[1][2] + t_node[0][2],
                                    t_node[1][3]
                                ),
                                t_node[2] - 1
                            )
            if t_node[2] >= 1:
                t_node = (
                                (
                                t_node[0][0] + 1,
                                t_node[0][1],
                                t_node[0][2]
                                ),
                                (
                                t_node[1][0] - blueprint[0] + t_node[0][0],
                                t_node[1][1] - blueprint[1] + t_node[0][1],
                                t_node[1][2] - blueprint[2] + t_node[0][2],
                                t_node[1][3]
                                ),
                                t_node[2] - 1
                            )

                max_geodes = dfs(t_node, blueprints, max_ing, visited, max_geodes)
    
    return max_geodes


def main():
    blueprint_lists = get_data()
    total = 0
    for i, blueprints in enumerate(blueprint_lists):
        total += (i+1) * dfs(((1, 0, 0), (0, 0, 0, 0), 24), blueprints, tuple(max(x) for x in zip(*blueprints)))
        print(total)

    print(total)

if __name__ == '__main__':
    main()