
T = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]

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
    def __init__(self, vertices, arr):
        self.V = vertices
        self.nodes = arr
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

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def add_path(self):
        for path in range(len(self.nodes)):
            self.add_edge(path, self.nodes[path])
            #print("path1 =",path, self.nodes[path])
            #self.graph[self.nodes[path]] = set([].append(path))
        return self.graph

    def find_root(self):
        for city in range(len(self.nodes)):
            if self.nodes[city] is city:
                return city
        # If no root node
        return -1

if __name__ == "__main__":
    cities = len(T)
    graph = Graph(cities, T)
    root = graph.find_root()
    print("root = ", root)
    print("path =", graph.add_path())

    graph.print_graph()
