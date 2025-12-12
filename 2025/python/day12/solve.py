from aocd import get_data, submit

YEAR = 2025


def get_unique_rotations_and_flips(coords):
    """
    Generates unique 90-degree rotations about (1,1), 
    INCLUDING flipped (mirrored) variants.
    """
    unique_shapes = set()
    
    def rotate_shape(shape):
        return [(c, 2 - r) for r, c in shape]

    def flip_shape(shape):
        return [(r, 2 - c) for r, c in shape]
    base_configurations = [coords, flip_shape(coords)]
    for config in base_configurations:
        current_coords = config
        
        for _ in range(4):
            shape_signature = tuple(sorted(current_coords))
            unique_shapes.add(shape_signature)
            current_coords = rotate_shape(current_coords)

    return [list(shape) for shape in unique_shapes]


def part1(data):
    l = data.split("\n\n")
    SHAPE_SIZE = 3
    *shapes, area = l
    shapes = [s.split(":")[1].strip().split("\n") for s in shapes]
    new_shapes = []
    for s in shapes:
        new_shapes.append([(i, j) for i in range(len(s)) for j in range(len(s[0])) if s[i][j] == "#"])
    shapes = new_shapes
    shapes = [get_unique_rotations_and_flips(shape) for shape in shapes]
    t = 0

    for line in area.split("\n"):
        dims, shape_counts = line.split(": ")
        width, height = map(int, dims.split("x"))
        shape_counts = list(map(int,shape_counts.split()))
        # This day is stupid
        if width * height >= sum(len(shapes[i][0])*shape_counts[i] for i in range(len(shapes))):
            t += 1
        
        # states = set()
        # states.add(frozenset())
        # i = 0
        # while states:
        #     print(len(states))
        #     new_states = set()
        #     done = False
        #     while shape_counts[i] == 0:
        #         i += 1
        #         if i == len(shape_counts):
        #             done = True
        #             break
        #     if done:
        #         break

        #     next_shape = shapes[i]
        #     shape_counts[i] -= 1
        #     for state in states:
        #         for y in range(height - SHAPE_SIZE + 1):
        #             for x in range(width - SHAPE_SIZE + 1):
        #                 for rot in shapes[i]:
        #                     coords = set((old_y + y, old_x + x) for old_y, old_x in rot)
        #                     for coord in coords:
        #                         if coord in state:
        #                             break
        #                     else:
        #                         new_states.add(state|coords)
            
        #     states = new_states
                            
        
        # if states:
        #     t += 1
                
    print(t)
    return None


def part2(data):
    l = data.split("\n")
    return None


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
