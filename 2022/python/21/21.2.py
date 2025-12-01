from os.path import dirname, join

def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./21i.txt")

    with open(path) as f:
        unpacked = [line.strip('\n').split() for line in f.readlines()]
        return {x[0][:-1]: x[1:] for x in unpacked}


def dfs_recursive(start_node, total=0):
    if len(node_dict[start_node]) == 1:
        return int(node_dict[start_node][0])
    
    left = dfs_recursive(node_dict[start_node][0], total)
    right = dfs_recursive(node_dict[start_node][2], total)
    match node_dict[start_node][1]:
        case '+':
            total += left + right
        case '-':
            total += left - right
        case '*':
            total += left * right
        case '/':
            total += left // right
    
    return total


def reverse_dfs(current_node):
    num_to_reach = 0
    while current_node != 'humn':
        # print(num_to_reach)
        # print(current_node)
        # print(''.join(node_dict[current_node]))
        try:
            total = dfs_recursive(node_dict[current_node][0])
            print(node_dict[current_node][0], '=', total)
            match node_dict[current_node][1]:
                case '+':
                    num_to_reach -= total
                case '-':
                    num_to_reach = -1 * (num_to_reach - total)
                case '*':
                    num_to_reach = num_to_reach // total
                case '/':
                    num_to_reach = num_to_reach // total
                case '=':
                    num_to_reach = total
            current_node = node_dict[current_node][2]
        except:
            total = dfs_recursive(node_dict[current_node][2])
            print(node_dict[current_node][2], '=', total)
            match node_dict[current_node][1]:
                case '+':
                    num_to_reach -= total
                case '-':
                    num_to_reach += total
                case '*':
                    num_to_reach = num_to_reach // total
                case '/':
                    num_to_reach *= total
                case '=':
                    num_to_reach = total
            current_node = node_dict[current_node][0]
        
        # print()

    return num_to_reach



def main():
    global node_dict
    node_dict = get_data()
    node_dict['humn'] = None
    node_dict['root'][1] = '='
    print(reverse_dfs('root'))

if __name__ == '__main__':
    main()
    