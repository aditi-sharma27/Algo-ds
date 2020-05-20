"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

# A class to represent the adjacency list of the node


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def find_root(self, arr):
        for city in range(len(arr)):
            if arr[city] is city:
                return city
        # If no root node
        return -1

    # Function to print the graph
    def print_graph(self):
        d = {}
        l = []
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            print("\ntemp ==", temp)
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def dict_list(self):
        adj_dict = { i: self.graph[i] for i in range(len(graph))}
        print("adj = ", adj_dict)

 # Function to print a BFS of graph
    def bfs(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        level = [0] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        level[s] = 0
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            print("vertex", type(self.graph[s]), self.graph[s].vertex)
            for i in self.graph[s].vertex:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    level[i] = level[s] +1
        print("level = ", level)

if __name__ == "__main__":
    T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
    V = len(T)
    graph = Graph(V)
    for i in range(len(T)):
        graph.add_edge(T[i], i)

    root = graph.find_root(T)
    print("root =", root)
    graph.dict_list()

    #graph.bfs(root)
