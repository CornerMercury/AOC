from aocd import get_data, submit

YEAR=2024

def part1(data):
    l, m = data.split("\n\n")
    d = {}
    for s in l.split('\n'):
        k, v = s.split(': ') 
        d[k] = int(v)
    
    rules = []
    for s in m.split('\n'):
        r, result = s.split (' -> ') 
        r = r.split()
        rules.append((r[0], r[2], r[1][0], result))
    
    while rules:
        for i in range(len(rules) - 1, -1, -1):
            a, b, o, r = rules[i]
            if not (a in d and b in d):
                continue
            a = d[a]
            b = d[b]
            rules.pop(i)
            t = 0
            if o == 'X':
                t = a != b
            elif o == 'A':
                t = a and b
            else:
                t = a or b

            d[r] = t

    z = []
    for key, value in d.items():
        if key[0] == 'z':
            z.append((key, int(value)))

    z = list(reversed(sorted(z)))
    z = map(lambda x : str(x[1]), z)
    z = int(''.join(z), 2)
    return z




def part2(data):
    l, m = data.split("\n\n")
    l = l.split('\n')
    
    rules = []
    for s in m.split('\n'):
        r, result = s.split (' -> ') 
        r = r.split()
        rules.append((r[0], r[2], r[1][0], result))
    
    c_rules = rules[::]
    
    carry_lookup = {}
    incorrect_pairs = set()
    for i in range(len(l) // 2):
        aXb = ''
        aAb = ''
        aA2b = ''

        x = f'x{i:0>2}'
        y = f'y{i:0>2}'
        for j in range(len(rules)):
            a, b, o, r = rules[j]
            if ((a == x and b == y) or (a == y and b == x)) and o == 'X':
                aXb = r
                rules.pop(j)
                break
        

        x = f'x{i:0>2}'
        y = f'y{i:0>2}'
        for j in range(len(rules)):
            a, b, o, r = rules[j]
            if ((a == x and b == y) or (a == y and b == x)) and o == 'A':
                aAb = r
                rules.pop(j)
                break
        
        if i != 0:
            x = aXb
            y = carry_lookup[f'c{i:0>2}']
            for j in range(len(rules)):
                a, b, o, r = rules[j]
                if ((a == x and b == y) or (a == y and b == x)) and o == 'X' and r == f'z{i:0>2}':
                    rules.pop(j)
                    break
            else:
                if y[0] == 'z':
                    incorrect_pairs.add(y)
                else:
                    for a, b, o, r in rules:
                        if ((a == x and b == y) or (a == y and b == x)) and o == 'X':
                            incorrect_pairs.add(r)
                            incorrect_pairs.add(f'z{i:0<2}')
                            break
                    else:
                        incorrect_pairs.add(tuple(sorted([x, y])))
            
            for j in range(len(rules)):
                a, b, o, r = rules[j]
                if ((a == x and b == y) or (a == y and b == x)) and o == 'A':
                    aA2b = r
                    rules.pop(j)
                    break
            else:
                for a, b, o, r in rules:
                    if ((a == x) or (b == x) or (a == y) or (b == y)) and o == 'A':
                        aA2b = r
                        break
                if y[0] == 'z':
                    incorrect_pairs.add(y)
                else:
                    incorrect_pairs.add(tuple(sorted([x, y])))

            x = aAb
            y = aA2b
            for j in range(len(rules)):
                a, b, o, r = rules[j]
                if ((a == x and b == y) or (a == y and b == x)) and o == 'O':
                    carry_lookup[f'c{i + 1:0>2}'] = r
                    rules.pop(j)
                    break
            else:
                for a, b, o, r in rules:
                    if ((a == x) or (b == x) or (a == y) or (b == y)) and o == 'O':
                        carry_lookup[f'c{i + 1:0>2}'] = r
                        if (a == x) or (b == x):
                            incorrect = y
                            correct = x
                        else:
                            incorrect = x
                            correct = y
                        
                        incorrect_pairs.add(incorrect)

                        for _, _, o, r in c_rules:
                            if r == correct:
                                break
                        if o == 'O':
                            x = f'x{i:0>2}'
                            y = f'y{i:0>2}'
                            for a, b, o, r in c_rules:
                                if ((a == x and b == y) or (a == y and b == x)) and o == 'X':
                                    incorrect_pairs.add(r)
                        else:
                            pass
                            
                

            continue

        carry_lookup[f'c{i + 1:0>2}'] = aAb
        

    return ",".join(sorted(map(lambda x: x[0] if isinstance(x, tuple) else x, incorrect_pairs)))

        
            


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
