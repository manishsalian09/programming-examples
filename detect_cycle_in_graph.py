from collections import defaultdict
class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)] 
        self.parent = [i for i in range(vertices)]
        self.rank = [0] * vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.parent[u] = u

    def print_graph(self):
        for i in range(self.vertices):
            print(str(i) + " edge = " + str(self.graph[i]))

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex

        self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 == root2:
            return False
        
        if self.rank[root1] >= self.rank[root2]:
            if self.rank[root1] == self.rank[root2]: self.rank[root1] += 1
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2

        return True
            

    def has_cycle(self):
        for i in range(self.vertices):
            parent1 = self.find(i)
            for j in self.graph[i]:
                parent2 = self.find(j)

                if parent1 == parent2:
                    return True

                self.union(parent1, parent2)
        return False

graph = Graph(3)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)

#graph = Graph(5)
#graph.add_edge(0, 1)
#graph.add_edge(1, 2)
#graph.add_edge(2, 3)
#graph.add_edge(3, 4)
#graph.add_edge(4, 2)

#graph = Graph(5)
#graph.add_edge(0, 1)
#graph.add_edge(1, 2)
#graph.add_edge(1, 3)
#graph.add_edge(3, 4)

graph.print_graph()
     
if graph.has_cycle():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")

