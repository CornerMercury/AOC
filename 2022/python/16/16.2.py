from os.path import dirname, join
import copy
class Mover:
    def __init__(self, current_node, waiting_time=0):
        self.current_node = current_node
        self.waiting_time = waiting_time

    def __str__(self):
        return f'(n: {self.current_node}, t: {self.waiting_time})'

class State:
    def __init__(self, movers, pressure=0, activated=set()):
        self.pressure = pressure
        # Holds list of moving things i.e. human and
        # their current node and waiting time until
        # they can move again
        self.movers = movers
        self.activated = activated

    def __str__(self):
        return f'p: {self.pressure}, activated: {", ".join([item for item in self.activated])}'



def bfs(connections, node_info, start_node, time_limit):
    time = 0
    branches = {State([Mover(start_node) for _ in range(2)], activated={start_node})}
    finished_branches = set()
    max_time_from_start = max(connections[start_node].values())
    print(max_time_from_start)

    while time < time_limit - 1:
        # for branch in branches:
        #     print(branch)
        #     print(branch.movers[0])
        time += 1
        print('----', time, '----')
        new_branches = set()
        print(len(branches))
        for branch in branches:
            for i, mover in enumerate(branch.movers):
                if mover.waiting_time != 0:
                    mover.waiting_time -= 1
                    new_branches.add(branch)
                    continue
                if mover.current_node not in branch.activated:
                    new_state = copy.deepcopy(branch)
                    new_state.activated.add(mover.current_node)
                    new_state.pressure += (time_limit - time) * node_info[mover.current_node][0]
                    if len(new_state.activated) == len(connections[mover.current_node]):
                        finished_branches.add(new_state)
                    else:
                        new_branches.add(new_state)

                    continue

                for neighbour, weight in connections[mover.current_node].items():
                    new_state = copy.deepcopy(branch)
                    new_state.movers[i].current_node = neighbour
                    new_state.movers[i].waiting_time = weight - 1
                    new_branches.add(new_state)

        branches = new_branches

    return finished_branches.union(branches)


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./16i.txt")

    with open(path) as f:
        data = [line.strip('\n').split() for line in f.readlines()]
    connection_valves = {}
    valves = {}
    nodes = {}
    for line in data:
        name = line[1]
        rate = int(line[4].split('=')[1][:-1])
        connections = ''.join(line[9:]).split(',')
        
        if rate == 0 and name != 'AA':
            connection_valves[name] = connections
        else:
            valves[name] = (rate, connections)
            nodes[name] = {}

        
        
    for key, value in valves.items():
        for node in value[1]:
            weight = 1
            last_node = key
            current_node = node
            while current_node not in valves:
                edges = connection_valves[current_node]
                if edges[0] == last_node:
                    last_node = current_node
                    current_node = edges[1]
                else:
                    last_node = current_node
                    current_node = edges[0]
                
                weight += 1

            nodes[key][current_node] = weight
            nodes[current_node][key] = weight
        

    return valves, nodes


def main():
    valves, nodes = get_data()
    print(nodes)
    states = bfs(nodes, valves, 'AA', 26)
    max_pressure = 0
    for state in states:
        if state.pressure > max_pressure:
            max_pressure = state.pressure
            print(state)
    
    print(max_pressure)

if __name__ == '__main__':
    main()