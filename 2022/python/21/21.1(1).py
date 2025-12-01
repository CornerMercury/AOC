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

def main():
    global node_dict
    node_dict = get_data()
    print(dfs_recursive('root'))

if __name__ == '__main__':
    main()
    