"""""
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
0  -1 INF INF

3  -1   0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4

0 is gate 
-1 is wall
INF -> to solve get to the nearest gate
"""""

INF = 999999
grid = [[INF, -1, 0, INF],[INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]

def dfs_solve_path(grid):

    all_gates = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                all_gates.append((i,j))

    # run dfs on these gates
    distance = 0
    while all_gates:
        distance += 1
        next_gates = []
        for gate in all_gates:
            x,y = gate
            for node in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0]) and grid[node[0]][node[1]] == INF:
                    grid[node[0]][node[1]] = distance
                    next_gates.append(node)
        all_gates = next_gates


dfs_solve_path(grid)
print(grid)
