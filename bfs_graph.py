from queue import Queue
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]
        self.visited = [False for v in range(vertices)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        if (start_vertex >= self.vertices or start_vertex < 0): return
        
        queue = Queue()
        queue.put(start_vertex)
        while (not queue.empty()):
            vertex = queue.get()
            if (not self.visited[vertex]):
                self.visited[vertex] = True
                print(vertex, end = " ")
                for adjacent_vertex in self.graph[vertex]: 
                    queue.put(adjacent_vertex)
        print()

    def print_graph(self):
        for v in range(self.vertices):
            print("vertex = " + str(v) + " edge = " + str(self.graph[v]) , end = " ")
            print()

graph = Graph(6)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(1, 4)
graph.addEdge(4, 5)
graph.addEdge(3, 5)
print ("---------Graph-------")
graph.print_graph()
print("---------BST---------")
graph.bfs(0)
