from aocd import get_data, submit
from collections import deque
from copy import deepcopy

YEAR = 2023


def part1(data):
    rules, workflows = data.split("\n\n")
    workflows = [
        eval(workflow.replace("=", '":').replace("{", '{"').replace(",", ',"'))
        for workflow in workflows.split("\n")
    ]
    rules_dict = {}
    for rule_set in rules.split("\n"):
        rule_list = []
        key, rest = rule_set.split("{")
        rest = rest[:-1]
        for rule in rest.split(","):
            if ":" not in rule:
                rule_list.append(("True", rule))
                continue
            rule_list.append(tuple(rule.split(":")))
        rules_dict[key] = rule_list

    res = 0
    for workflow in workflows:
        locals().update(workflow)
        key = "in"
        while key != "A" and key != "R":
            for rule, key in rules_dict[key]:
                if eval(rule):
                    break
        if key == "A":
            res += sum(workflow.values())

    return res


def part2(data):
    rules, _ = data.split("\n\n")
    rules_dict = {}
    for rule_set in rules.split("\n"):
        rule_list = []
        key, rest = rule_set.split("{")
        rest = rest[:-1]
        for rule in rest.split(","):
            if ":" not in rule:
                rule_list.append(rule)
                continue
            rule_list.append(tuple(rule.split(":")))
        rules_dict[key] = rule_list

    # ([(var, range_start, range_end)])
    s = deque([["in", {c: [1, 4000] for c in "xmas"}]])
    res = 0
    while s:
        key, range_dict = s.pop()
        if key == "A":
            out = 1
            for sr, er in range_dict.values():
                out *= er - sr + 1
            res += out
            continue
        elif key == "R":
            continue
        for rule, new_key in rules_dict[key][:-1]:
            var = rule[0]
            operator = rule[1]
            num = int(rule[2:])
            if operator == "<":
                # 01(
                if range_dict[var][1] < num:
                    s.append([new_key, range_dict])
                    break
                # 0(1
                elif range_dict[var][0] < num:
                    temp = range_dict[var][1]
                    range_dict[var][1] = num - 1
                    s.append([new_key, deepcopy(range_dict)])
                    range_dict[var] = [num, temp]
                # (01
            else:
                # )01
                if range_dict[var][0] > num:
                    s.append([new_key, range_dict])
                    break
                # 0)1
                elif range_dict[var][1] > num:
                    temp = range_dict[var][0]
                    range_dict[var][0] = num + 1
                    s.append([new_key, deepcopy(range_dict)])
                    range_dict[var] = [temp, num]
                # 01)
        else:
            s.append([rules_dict[key][-1], range_dict])
    return res


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
