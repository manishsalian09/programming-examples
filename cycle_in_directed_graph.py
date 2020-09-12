class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]
        self.white_set = {i for i in range(vertices)}
        self.grey_set = set()
        self.black_set = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle(self):
        while self.white_set:
            if self.dfs(self.white_set.pop()):
                return True
        return False

    def dfs(self, current_vertex):
        self.grey_set.add(current_vertex)
        self.white_set.discard(current_vertex)

        for v in self.graph[current_vertex]:
            if v in self.black_set:
                continue
            
            if v in self.grey_set:
                return True
            
            if self.dfs(v):
                return True

        self.black_set.add(current_vertex)
        self.grey_set.remove(current_vertex)
        return False

    def print_graph(self):
        for v in range(self.vertices):
            print("vertex = " + str(v) + " edge = " + str(self.graph[v]))

    def print_sets(self):
        print(self.white_set)
        print(self.grey_set)
        print(self.black_set)

graph = Graph(6)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(3, 0)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
#graph.add_edge(5, 3)
graph.print_graph()

#graph.print_sets()
if graph.has_cycle():
    print("Has cycle")
else:
    print("Does not have cycle")


#graph.print_sets()

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 1)
graph.print_graph()

if g.has_cycle():
    print("Has cycle")
else:
    print("Does not have cycle")


