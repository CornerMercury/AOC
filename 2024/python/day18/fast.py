from aocd import get_data, submit

YEAR=2024

def part1(data):
    l = data.split("\n")
    blocks = set()
    for i in range(1024):
        s = l[i].split(",")
        blocks.add((int(s[1]), int(s[0])))
    
    SIZE = 70
    queue = [(0, 0, 0)]
    visited = set()
    while queue:
        y, x, weight = queue.pop(0)
        if not (0 <= y <= SIZE) or not (0 <= x <= SIZE) or (y, x) in blocks or (y, x) in visited:
            continue
        if (y, x) == (SIZE, SIZE):
            return weight

        
        visited.add((y, x))
        queue.append((y, x - 1, weight + 1))
        queue.append((y - 1, x, weight + 1))
        queue.append((y + 1, x, weight + 1))
        queue.append((y, x + 1, weight + 1))

def part2(data):
    l = data.split("\n")
    SIZE = 70
    low = 0
    high = len(l) - 1
    for i in range(len(l)):
        s = l[i].split(",")
        l[i] = (int(s[1]), int(s[0]))
    while low < high:
        mid = (low + high) // 2
        
        blocks = set()
        for i in range(mid):
            blocks.add(l[i])
    
        queue = [(0, 0, 0)]
        visited = set()
        while queue:
            y, x, weight = queue.pop(0)
            if not (0 <= y <= SIZE) or not (0 <= x <= SIZE) or (y, x) in blocks or (y, x) in visited:
                continue
            if (y, x) == (SIZE, SIZE):
                low = mid + 1
                break
            
            visited.add((y, x))
            queue.append((y, x - 1, weight + 1))
            queue.append((y - 1, x, weight + 1))
            queue.append((y + 1, x, weight + 1))
            queue.append((y, x + 1, weight + 1))
        else:
            high = mid - 1
        i += 1
    
    if mid != low:
        return f'{l[low][1]},{l[low][0]}'
    else:
        return f'{l[high][1]},{l[high][0]}'


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
