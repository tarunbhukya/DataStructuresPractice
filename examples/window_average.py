"""""
Input :
-1 is wall
INF to find close to 0
0 is Gate

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

OutPut:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""""
INF = 999999
rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
rooms1 = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]

def wallsAndGates(rooms):
    queue = []
    i,j = find_next_INF_node(rooms)

    if i is not None:
        process_shortest_path(i,j, rooms)

    print("=================")
    i,j = find_next_INF_node(rooms)
    while i is not None:
        process_shortest_path(i,j, rooms)
        i, j = find_next_INF_node(rooms)

    print("=================")
    # i, j = find_next_INF_node(rooms)
    # if i is not None:
    #     process_shortest_path(i, j, rooms)

    print(rooms)




def find_next_INF_node(rooms):
    # Imagine rooms as a graph or a tree, consider 0,0 as a root node
    print("tarun")
    print(rooms)
    for i in range(len(rooms)):
        for j in range(len(rooms[0])):
            if rooms[i][j] == INF:
                # The main aim is to find the shorted path from INF to 0 without having -1(wall) in between
                print("what {}, {} is {}".format(i,j,rooms[i][j]))
                return i,j

    return None, None


def process_shortest_path(i, j, rooms):
    print("process {}, {}".format(i,j))
    hashmap = {}
    queue = []
    queue.append((i,j))
    # process the node by popping it
    # whenever processed add it to hashmap and value to be 0
    while len(queue) != 0:
        print(queue)
        i,j = queue.pop()
        print("pooping {}, {}".format(i,j))
        node = rooms[i][j]

        # add all its child nodes to the queue only when if it is INF
        if node == INF:

            # add +1 for all keys which are found till now: Hint level order traversal for shortest path
            increment_hash_values(hashmap)

            key = "{},{}".format(i, j)
            hashmap[key] = 0
            rows = len(rooms)
            columns = len(rooms[0])

            # since every node has some children
            if j < columns-1:
                # if rooms[i][j+1] > 0 and rooms[i][j+1] != INF:
                #     rooms[i][j] = rooms[i][j+1] + 1
                #     return True
                if rooms[i][j+1] == INF or rooms[i][j+1] == 0 :
                    queue.append((i,j+1))

            if i < rows-1:
                # if rooms[i+1][j] > 0 and rooms[i+1][j] != INF:
                #     rooms[i][j] = rooms[i+1][j] + 1
                #     return True
                if rooms[i+1][j] == INF or rooms[i+1][j] == 0:
                    queue.append((i+1, j))


            if i > 0:
                if rooms[i-1][j] > 0 and rooms[i-1][j] != INF:
                    rooms[i][j] = rooms[i-1][j] + 1
                    return True
                key = "{},{}".format(i-1, j)
                if (rooms[i-1][j] == INF or rooms[i-1][j] == 0 ) and hashmap.get(key, None) is None :
                    queue.append((i - 1, j))

            if j > 0:
                # if rooms[i][j-1] > 0 and rooms[i][j-1] != INF:
                #     rooms[i][j] = rooms[i][j-1] + 1
                #     return True
                key = "{},{}".format(i, j-1)
                if (rooms[i][j - 1] == INF or rooms[i][j - 1] == 0 ) and hashmap.get(key, None) is None:
                    queue.append((i, j - 1))

        if node == 0:
            increment_hash_values(hashmap)
            process_hash_to_rooms(hashmap, rooms)
            return True



def increment_hash_values(hash):
    for i in hash.keys():
        hash[i] += 1

def process_hash_to_rooms(hash, rooms):
    for key in hash.keys():
        i,j = key.split(",")
        print("{}, {}".format(i,j))
        rooms[int(i)][int(j)] = hash[key]


wallsAndGates(rooms)
print(rooms)