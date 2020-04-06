from collections import deque

# adjacency list
g = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

g1 = {1: [2, 5, 3], 2: [6, 4], 5: [4], 3: [4, 7]}

def bfs(graph, s):
    queue = deque([s])
    level = {s: 0}
    parent = {s: None}
    while queue:
        vertex = queue.popleft()
        print(queue)
        print("vertex = ", vertex)
        if vertex in graph:
            for nbr in graph.get(vertex):
                if nbr not in level:
                    queue.append(nbr)
                    level[nbr] = level[vertex] + 1
                    parent[nbr] = vertex
                    print("level = ", level)
                    #print("parent =", parent)

#bfs(g, 'A')
bfs(g1, 1)

print(graph.get(2))

