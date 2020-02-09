grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def path_finder(grid, target):
    return bfs_shortest_path(grid, target)


def bfs_shortest_path(graph, target):
    if graph is None:
        return False

    path_map = {}
    next_nodes = []
    visited_set = set()
    x, y = 0, 0
    next_nodes.append((x, y))
    next_nodes.append((-1,-1))
    count = 0

    while len(next_nodes) != 0:
        x,y = next_nodes.pop(0)

        if len(visited_set) == len(graph) * len(graph[0]):
            return False

        if x == -1 and y == -1:
            next_nodes.append((-1,-1))
            count += 1
            continue

        if graph[x][y] == target:
            print(print_path(x, y, path_map))
            return count

        visited_set.add((x,y))
        add_adjacent_nodes(graph, x, y, next_nodes, visited_set, path_map)


def add_adjacent_nodes(graph, x, y, next_nodes, visited_set, path_map):
    if x < len(graph) - 1 and not visited_set.__contains__((x+1,y)):
        next_nodes.append((x+1,y))
        path_map[(x+1,y)] = [(x,y),(x+1,y)]
    if y < len(graph[0]) - 1 and not visited_set.__contains__((x,y+1)):
        next_nodes.append((x,y+1))
        path_map[(x,y+1)] = [(x,y),(x,y+1)]


def print_path(x, y, path_map):
    queue = path_map.get((x,y))
    if x == 0 and y == 0:
        return [(0,0)]
    while path_map.get(queue.__getitem__(0)) is not None:
        add_nodes = []
        add_nodes = path_map.get(queue.pop(0))
        add_nodes.extend(queue)
        queue = add_nodes
    return queue

print("number of steps : "  + str(path_finder(grid, 3)))
