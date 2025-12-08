from aocd import get_data, submit
from collections import deque

YEAR = 2025


def part1(data):
    l = data.split("\n")
    nodes = [(int(a),int(b),int(c)) for a,b,c in map(lambda x: x.split(","), l)]
    distances = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            left = nodes[i]
            right = nodes[j]
            distance = ((left[0] - right[0])**2 + (left[1] - right[1])**2 + (left[2] - right[2])**2)**0.5
            distances.append((distance, i, j))
    
    edges = {}
    for _, i, j in sorted(distances)[:1000]:
        edges[i] = edges.get(i, []) + [j]
        edges[j] = edges.get(j, []) + [i]
    
    visited = set()
    subgraphs = []
    for node in edges.keys():
        if node not in visited:
            component = []
            queue = deque([node])
            visited.add(node)
            while queue:
                current = queue.popleft()
                component.append(current)
                
                for neighbor in edges[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            subgraphs.append(component)

    lens = sorted(map(len,subgraphs))
    return lens[-1]*lens[-2]*lens[-3]


def part2(data):
    l = data.split("\n")
    nodes = [(int(a),int(b),int(c)) for a,b,c in map(lambda x: x.split(","), l)]
    distances = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            left = nodes[i]
            right = nodes[j]
            distance = ((left[0] - right[0])**2 + (left[1] - right[1])**2 + (left[2] - right[2])**2)**0.5
            distances.append((distance, i, j))
    
    distances = sorted(distances)
    for pairs in range(len(nodes)-1, len(distances)):
        edges = {}
        for _, i, j in distances[:pairs]:
            edges[i] = edges.get(i, []) + [j]
            edges[j] = edges.get(j, []) + [i]
        
        visited = set()
        subgraphs = []
        for node in edges.keys():
            if node not in visited:
                component = []
                queue = deque([node])
                visited.add(node)
                while queue:
                    current = queue.popleft()
                    component.append(current)
                    
                    for neighbor in edges[current]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                subgraphs.append(component)

        if len(subgraphs) == 1:
            break

    return nodes[i][0] * nodes[j][0]


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
