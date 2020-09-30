""" 
    total vertex V
    build a graph
    sort the edges in asc order of weight and store it in a sorted list
    create a empty mst
    traverse till V-1 is reached
    if edge in sorted list doesn't have a cycle add it in mst else discard

"""

from queue import Queue 

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.visited = [False for v in range(vertices)]
        self.graph = []
        self.parent = [i for i in range(vertices)]
        self.rank = [0] * vertices

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def mst(self):
        mst_graph = []
        org_graph = sorted(self.graph, key = lambda v : v[2])
        for edge in org_graph:
            if len(mst_graph) == self.vertices - 1:
                break;

            parent1 = self.find(edge[0])
            parent2 = self.find(edge[1])

            if parent1 != parent2:
                mst_graph.append(edge)
                self.union(parent1, parent2)

        print("sorted graph\n-------------------")
        self.print_graph(org_graph)
        print("MST\n-------------------")
        self.print_graph(mst_graph)

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

    def print_graph(self, graph):
        for e in graph:
            print(e)

graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 7, 8)
graph.add_edge(1, 2, 8)
graph.add_edge(1, 7, 11)
graph.add_edge(7, 6, 1)
graph.add_edge(7, 8, 7)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 5, 4)
graph.add_edge(2, 8, 2)
graph.add_edge(8, 6, 6)
graph.add_edge(6, 5, 2)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 14)
graph.add_edge(5, 4, 10)
graph.print_graph(graph.graph)
graph.mst()
