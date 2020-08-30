"""
    Dijkstra's Algo
"""
from queue import Queue 

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.visited = [False for v in range(vertices)]
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, vertex, adjacent_vertex, weight):
        self.graph.append(vertex)
        #self.graph[vertex].append((adjacent_vertex, weight))
        self.graph[vertex].append({"vertex": adjacent_vertex, "weight": weight})

    def print_shortest_path(self, source_vertex, target_vertex):
        path = []
        distance = 0

        queue = Queue()
        queue.put(source_vertex)
        path.append(source_vertex)
        while not queue.empty():
            current_vertex = queue.get()
            
            if target_vertex == current_vertex:
                break;

            if not self.visited[current_vertex]:
                next_vertex = {'vertex': float('inf'), 'weight': float('inf')}
                
                # find next vertex with minimum distance
                for adjacent_vertex in self.graph[current_vertex]:
                    if next_vertex['weight'] > adjacent_vertex['weight']:
                        next_vertex = adjacent_vertex
                
                queue.put(next_vertex['vertex'])
                path.append(next_vertex['vertex'])
                distance = distance + next_vertex['weight']
                self.visited[current_vertex] = True

        print("shortest path = " + str(path) + ", minimum distance = " + str(distance))

    def print_graph(self):
        for v in range(self.vertices):
            print("vertex = " + str(v) + " edge = " + str(self.graph[v]) , end = " ")
            print()

graph = Graph(6)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 10)
graph.add_edge(2, 4, 3)
graph.add_edge(4, 3, 4)
graph.add_edge(3, 5, 11)
graph.print_graph()
graph.print_shortest_path(0, 5)

