from os.path import dirname, join
from itertools import product
from copy import deepcopy


def dfs(state, max_pressure=0):
    # state = {
    #     'pressure': int,
    #     'activated': set,
    #     'time_left': int,
    #     'movers': (
    #             {
    #                 'current_node': str,
    #                 'waiting_time': int
    #             },
    #             {...}
    #         )
    # }

    if len(state['activated']) == len(node_info) or state['time_left'] == 0:
        if max_pressure < state['pressure']:
            print(state)
            return state['pressure']
        else:
            return max_pressure
    
    if max_pressure > 81 * (state['time_left'] - 1) + state['pressure']:
        return max_pressure


    mover_possibilities = []
    for mover in state['movers']:
        if mover['waiting_time'] != 0:
            mover_possibilities.append([(mover['current_node'], 0)])
        else:
            mover_possibilities.append([(mover['current_node'], 1)] + [neighbour_info for neighbour_info in connection_info[mover['current_node']]])

    for branch in product(*mover_possibilities):
        new_state = deepcopy(state)
        new_state['time_left'] -= 1
        for i, mover_info in enumerate(zip(state['movers'], branch)):
            mover, mover_path = mover_info
            if mover['current_node'] == mover_path[0] and mover_path[1] == 1:
                if mover_path[0] in new_state['activated']:
                    break
                new_state['activated'].add(mover_path[0])
                new_state['time_activated'].append((mover_path[0], 26-state['time_left']))
                new_state['pressure'] += new_state['time_left'] * node_info[mover_path[0]][0]

            new_state['movers'][i]['current_node'] = mover_path[0]
            new_state['movers'][i]['waiting_time'] += mover_path[1] - 1

        else:
            max_pressure = dfs(new_state, max_pressure)

    return max_pressure



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
    global node_info, connection_info, average_pressure_release
    node_info, connection_info = get_data()
    connection_info = {node: sorted(value.items(), key=lambda x: x[1]) for node, value in connection_info.items()}
    average_pressure_release = int(sum(item[0] for item in node_info.values()) * 2.5 // len(node_info))
    start_state = {
                'pressure': 0,
                'activated': {'AA'},
                'time_activated': [0],
                'time_left': 26,
                'movers': (
                        {
                            'current_node': 'AA',
                            'waiting_time': 0
                        },
                        {
                            'current_node': 'AA',
                            'waiting_time': 0
                        },
                    )
            }
    print(dfs(start_state))


if __name__ == '__main__':
    main()