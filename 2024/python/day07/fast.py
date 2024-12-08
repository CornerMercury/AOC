from aocd import get_data, submit

YEAR=2024

def part1(data):
    def recurse(operands, target, current=0):
        if not operands:
            if target == current:
                return True
            return False
        a = False
        b = operands.pop(0)
        a |= recurse(operands, target, current + b)
        if a:
            return a
        a |= recurse(operands, target, current * b)
        operands.insert(0, b)
        return a
    l = data.split("\n")
    t=0
    for s in l:
        target, operands = s.split(":")
        operands = list(map(int, operands.split()))
        t += recurse(operands, int(target)) and int(target)
    return t


def part2(data):
    def recurse(operands, target, current=0):
        if not operands:
            if target == current:
                return True
            return False
        a = False
        b = operands.pop(0)
        a |= recurse(operands, target, current + b)
        if a:
            return a
        a |= recurse(operands, target, current * b)
        if a:
            return a
        a |= recurse(operands, target, int(str(current) + str(b)))
        operands.insert(0, b)
        return a
    l = data.split("\n")
    t=0
    for s in l:
        target, operands = s.split(":")
        operands = list(map(int, operands.split()))
        t += recurse(operands, int(target)) and int(target)
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
