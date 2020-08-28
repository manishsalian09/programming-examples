class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for v in range(n)]
        self.visited = [False for v in range(n)]

    def add_vertex(self, vertex):
        self.graph.append(vertex)

    def add_edge(self, vertex, adjacent_vertex):
        self.graph[vertex].append(adjacent_vertex)

    def print_graph(self):
        for v in range(self.n):
            print("vertex = " + str(v) + " edge = " + str(self.graph[v]) , end = " ")
            print()

class Matrix:
    def __init__(self, m, n):
        self.rows = m
        self.cols = n
        self.mat = [[] for i in range(m)]
        self.graph = [[] for v in range(m * n)]
        val = 0
        for i in range(m):
            for j in range(n):
                self.mat[i].append(val)
                val = val + 1

    def build_graph(self):
        graph = Graph(9)
        

    def print_matrix(self):
        for m in range(self.rows):
            print(self.mat[m])

"""
graph = Graph(9)
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(3, 6)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(6, 8)
graph.add_edge(7, 8)
graph.print_graph()
"""

matrix = Matrix(3, 3)
matrix.print_matrix()
