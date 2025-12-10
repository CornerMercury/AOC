from aocd import get_data, submit
from collections import deque
import pulp

YEAR = 2025


def part1(data):
    l = data.split("\n")
    total = 0
    for line in l:
        goal, *ms = line.split()
        buttons = ms[:-1]
        bin_goal = goal[1:-1][::-1].replace("#","1").replace(".","0")
        goal = int(bin_goal,2)
        bin_buttons = []
        for button in buttons:
            t = 0
            for b in button[1:-1].split(","):
                t += 2**int(b)
            bin_buttons.append(t)
        # BFS
        q = deque()
        q.append(goal)
        i = 0
        weights = {goal: 0}
        while q:
            v = q.popleft()
            if v == 0:
                total += weights[v]
                break
            for b in bin_buttons:
                n = v^b
                if n not in weights:
                    weights[n] = weights[v] + 1 
                    q.append(n)
        else:
            print(f"Solution not found for: {l}")        
            return

    return total


def part2(data):
    l = data.split("\n")
    total = 0
    for line in l:
        _, *buttons, goal = line.split()
        goal = tuple(map(int, goal[1:-1].split(",")))
        bin_buttons = [tuple(map(int, b[1:-1].split(",")))for b in buttons]

        prob = pulp.LpProblem("Button", pulp.LpMinimize)
        vars = pulp.LpVariable.dicts("Buttons", range(len(buttons)), cat='Integer', lowBound=0)
        prob += pulp.lpSum(vars[i] for i in range(len(vars)))
        for i in range(len(goal)):
            prob += pulp.lpSum(vars[j] for j in range(len(vars)) if i in bin_buttons[j]) == goal[i]
        prob.solve(pulp.GUROBI_CMD(msg=False))
        total += sum(pulp.value(vars[i]) for i in range(len(vars)))

    return total


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
