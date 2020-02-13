grid = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]

def number_of_islands(graph):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    lands = []
    lands_count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                bfs(i, j, directions, graph)
                lands_count += 1
    return lands_count

def bfs(i, j, directions, graph):
    if i<0 or i>=len(graph) or j<0 or j>=len(graph[0]):
        return
    if graph[i][j] == 1:
        graph[i][j] = "#"
        for direction in directions:
            bfs(i+direction[0], j+direction[1], directions, graph)





print(number_of_islands(grid))