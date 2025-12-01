from aocd import get_data, submit

YEAR=2024

def part1(data):
    s = data.strip()
    is_data = True
    id = 0
    disk = []
    for n in s:
        if is_data:
            disk += [id] * int(n)
            id += 1
        else:
            disk += [-1] * int(n)
        is_data = not is_data
    
    i=0
    j=len(disk) - 1
    while True:
        while disk[j] == -1:
            j -= 1
        while disk[i] != -1:
            i += 1
        if j <= i:
            break
        disk[i] = disk[j]
        disk[j] = -1

    
    t = 0
    i = 0
    while disk[i] != -1:
        t += disk[i] * i
        i += 1
    return t

def part2(data):
    s = data.strip()
    is_data = True
    id = 0
    disk = []
    for n in s:
        if is_data:
            disk += [id] * int(n)
            id += 1
        else:
            disk += [-1] * int(n)
        is_data = not is_data

    j = len(disk) - 1
    id = disk[-1]
    while id >= 0:
        while disk[j] != id:
            j -= 1
        size = 0
        while disk[j] == id:
            size += 1
            j -= 1
        j += 1
        i = 0
        while i < j:
            while disk[i] != -1:
                i += 1
            blank_size = 0
            while disk[i] == -1:
                blank_size += 1
                i += 1
            i -= 1
            if i < j and blank_size >= size:
                for index in range(0, size):
                    disk[i + 1 - blank_size + index] = id
                    disk[j + index] = -1
                break
            i += 1
        id -= 1

    t = 0
    for i in range(len(disk)):
        if disk[i] != -1:
            t += disk[i] * i

    return t


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
