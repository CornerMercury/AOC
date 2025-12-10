from aocd import get_data, submit
from collections import deque

YEAR = 2025
class DisjointSet:
    def __init__(self, n):
        # Initially, each element is its own parent (its own set)
        # [0, 1, 2, ... n]
        self.parent = list(range(n))
        
        # Rank is used to keep the trees flat during merging
        self.rank = [0] * n
        
        # Track the number of distinct collections
        self.num_collections = n

    def find(self, i):
        """
        Finds the representative (root) of the set containing i.
        Uses Path Compression to make future lookups O(1).
        """
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Merges the set containing i and the set containing j.
        Returns True if a merge happened, False if they were already merged.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by Rank: Attach smaller tree to larger tree
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            
            # Decrement the count of collections
            self.num_collections -= 1
            return True
        return False




def part1(data):
    l = data.split("\n")
    nodes = [(int(a),int(b),int(c)) for a,b,c in map(lambda x: x.split(","), l)]
    distances = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            left = nodes[i]
            right = nodes[j]
            distance = (left[0] - right[0])**2 + (left[1] - right[1])**2 + (left[2] - right[2])**2
            distances.append((distance, i, j))
    
    edges = {}
    for _, i, j in sorted(distances,key=lambda x:x[0])[:1000]:
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
    distances = [(((left:=nodes[i])[0] - (right:=nodes[j])[0])**2 + (left[1] - right[1])**2 + (left[2] - right[2])**2, i, j)for i in range(len(nodes))for j in range(i+1, len(nodes))]
    distances = sorted(distances,key=lambda x:x[0])
    dsu = DisjointSet(len(nodes))
    for _, i, j in distances:
        dsu.union(i,j)
        if dsu.num_collections == 1:
            return nodes[i][0] * nodes[j][0]

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
