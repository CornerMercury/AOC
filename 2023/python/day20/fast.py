from aocd import get_data, submit
from collections import deque, Counter
from math import prod

YEAR = 2023


class FlipFlop:
    def __init__(self):
        self.on = False

    def recieve(self, signal, _):
        if signal:
            return None
        self.on = not (self.on)
        return self.on


class Conjunction:
    def __init__(self, unreached_inputs):
        self.inputs = {}
        self.unreached_inputs = unreached_inputs

    def recieve(self, signal, inp):
        if inp not in self.inputs:
            self.unreached_inputs -= 1
        self.inputs[inp] = signal
        return bool(self.unreached_inputs) or not all(self.inputs.values())


def part1(data):
    l = data.split("\n")
    output_totals = Counter()
    for line in l:
        inp, outs = line.split(" -> ")
        outs = outs.split(", ")
        output_totals.update(Counter(outs))
        if inp == "broadcaster":
            starting_q = list(map(lambda x: ("broadcaster", x, False), outs))

    objects = {}
    for line in l:
        inp, outs = line.split(" -> ")
        outs = outs.split(", ")
        name = inp[1:]
        if inp[0] == "%":
            objects[name] = (FlipFlop(), outs)
        elif inp[0] == "&":
            objects[name] = (Conjunction(output_totals[name]), outs)

    counts = [0, 0]
    for _ in range(1000):
        counts[0] += len(starting_q) + 1
        q = deque(starting_q)
        while q:
            fro, to, signal = q.popleft()
            if to not in objects:
                continue
            obj, outs = objects[to]
            signal = obj.recieve(signal, fro)
            if signal == None:
                continue
            counts[signal] += len(outs)
            for out in outs:
                q.append((to, out, signal))
    return counts[0] * counts[1]


def part2(data):
    l = data.split("\n")
    last = "xm"
    output_totals = Counter()
    for line in l:
        inp, outs = line.split(" -> ")
        outs = outs.split(", ")
        output_totals.update(Counter(outs))
        if inp == "broadcaster":
            starting_q = list(map(lambda x: ("broadcaster", x, False), outs))

    objects = {}
    for line in l:
        inp, outs = line.split(" -> ")
        outs = outs.split(", ")
        name = inp[1:]
        if inp[0] == "%":
            objects[name] = (FlipFlop(), outs)
        elif inp[0] == "&":
            objects[name] = (Conjunction(output_totals[name]), outs)

    last_conjoins = {}
    i = 0
    while True:
        i += 1
        q = deque(starting_q)
        while q:
            fro, to, signal = q.popleft()
            obj, outs = objects[to]
            signal = obj.recieve(signal, fro)
            if signal == None:
                continue
            if outs == [last]:
                if signal and to not in last_conjoins:
                    last_conjoins[to] = i
                    if len(last_conjoins) == objects[last][0].unreached_inputs:
                        return prod(last_conjoins.values())
                continue
            for out in outs:
                q.append((to, out, signal))


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
