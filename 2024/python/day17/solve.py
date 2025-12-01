from aocd import get_data, submit

YEAR=2024

def part1(data):
    l, instr = data.split("\n\n")
    l = l.split("\n")
    a = int(l[0].split(": ")[1])
    b = int(l[1].split(": ")[1])
    c = int(l[2].split(": ")[1])

    instr = list(map(int,instr.split(": ")[1].split(",")))

    i = 0
    out = []
    while i < len(instr):
        if 0 <= instr[i + 1] <= 3:
            v = instr[i + 1]
        elif instr[i + 1] == 4:
            v = a
        elif instr[i + 1] == 5:
            v = b
        elif instr[i + 1] == 6:
            v = c

        match instr[i]:
            case 0:
                a //= (2 ** v)
            case 1:
                b ^= instr[i + 1]
            case 2:
                b = v % 8
            case 3:
                if a != 0:
                    i = instr[i + 1] - 2
            case 4:
                b ^= c
            case 5:
                out.append(str(v % 8))
            case 6:
                b = a // (2 ** v)
            case 7:
                c = a // (2 ** v)

        
        i += 2
    return ",".join(out)


def part2(data):
    data="""Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
    l, instr = data.split("\n\n")
    l = l.split("\n")
    da = 0
    db = int(l[1].split(": ")[1])
    dc = int(l[2].split(": ")[1])

    instr = list(map(int,instr.split(": ")[1].split(",")))
    print(instr)

    i = 0
    while True:
        out_index = 0
        a = da
        b = db
        c = dc
        while i < len(instr):
            if 0 <= instr[i + 1] <= 3:
                v = instr[i + 1]
            elif instr[i + 1] == 4:
                v = a
            elif instr[i + 1] == 5:
                v = b
            elif instr[i + 1] == 6:
                v = c

            match instr[i]:
                case 0:
                    a //= (2 ** v)
                case 1:
                    b ^= instr[i + 1]
                case 2:
                    b = v % 8
                case 3:
                    if a != 0:
                        i = instr[i + 1] - 2
                case 4:
                    b ^= c
                case 5:
                    if out_index < len(instr):
                        if instr[out_index] != v % 8:
                            break
                        out_index += 1 
                case 6:
                    b = a // (2 ** v)
                case 7:
                    c = a // (2 ** v)

            i += 2
        else:
            if out_index == len(instr):
                print(da)
                # return da
        da += 1


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
