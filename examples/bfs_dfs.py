grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]

def visit_nodes(grid):
    # visit_by_dfs(grid)
    print("#################")
    visit_by_bfs(grid)
    pass

def visit_by_dfs(grid):
    visited_queue = []
    if grid is None:
        return False
    i,j = 0,0

    visit_by_dfs_node(grid, i, j, visited_queue)

def visit_by_dfs_node(grid, x, y, visited_queue):
    if visited_queue.__contains__((x,y)):
        pass
    else:
        visited_queue.append((x,y))
        print("visited {} and {}".format(x,y))

        if y < len(grid[0]) - 1:
            y += 1
            visit_by_dfs_node(grid, x, y, visited_queue)

        if y > 0:
            y -=1
            visit_by_dfs_node(grid, x, y, visited_queue)

        if x < len(grid)-1:
            x += 1
            visit_by_dfs_node(grid, x, y, visited_queue)

        if x > 0:
            x -= 1
            visit_by_dfs_node(grid, x, y, visited_queue)

def visit_by_bfs(grid):
    next_nodes = []
    visited_nodes = set()
    x,y = 0,0
    next_nodes.append((x,y))
    visited_nodes.add((x, y))
    visit_by_bfs_node(grid, next_nodes, visited_nodes)

def visit_by_bfs_node(grid, next_nodes, visited_nodes):
    while len(next_nodes) != 0:
        # print("================")
        # print(next_nodes)
        # print(visited_nodes)
        # print("================")
        x,y = next_nodes.pop(0)
        print("x and y {} and {}".format(x,y))
        if x < len(grid) -1:
            if not visited_nodes.__contains__((x + 1, y)):
                next_nodes.append((x+1,y))
                visited_nodes.add((x+1, y))

        if y < len(grid[0]) -1:
            if not  visited_nodes.__contains__((x, y + 1)):
                next_nodes.append((x,y+1))
                visited_nodes.add((x, y+1))


visit_nodes(grid)
print(len(grid[0]))
