class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for v in range(vertices)]
        self.visited = [False] * vertices
        self.stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for v in range(self.vertices):
            print("vertex = " + str(v) + " edge = " + str(self.graph[v]))

    def search(self, current_vertex):
        if not self.visited[current_vertex]:
            self.visited[current_vertex] = True

        for v in self.graph[current_vertex]:
            if not self.visited[v]:
                self.search(v)
        
        self.stack.append(current_vertex)

    def sort(self):
        for v in range(self.vertices):
            if self.visited[v]:
                continue
            self.search(v)

        while self.stack:
            print(self.stack.pop(), end = " ")

graph = Graph(7)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 5)
graph.add_edge(4, 5)
graph.add_edge(5, 6)

graph.print_graph()
graph.sort()

