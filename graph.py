from collections import deque

from decorators.timer import timer

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return list(self.graph[vertex].keys())
        else:
            return []

    def get_weight(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            if (vertex1 == vertex2):
                return 0
            return self.graph[vertex1][vertex2]
        else:
            return None

    @timer(msg="Depth First Search")
    def dfs(self, start_vertex, target_vertex):
        visited = set()
        stack = [(start_vertex, [start_vertex], 0)]

        while stack:
            current_vertex, path, weight = stack.pop()

            if current_vertex == target_vertex:
                return (path, weight)

            visited.add(current_vertex)
            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], self.get_weight(current_vertex, neighbor) + weight))

        return None
    
    @timer(msg="Breadth First Search")
    def bfs(self, start_vertex, target_vertex):
        visited = set()
        queue = deque()

        queue.append((start_vertex, [start_vertex], 0))
        visited.add(start_vertex)

        while queue:
            current_vertex, path, weight = queue.popleft()

            if current_vertex == target_vertex:
                return (path, weight)

            neighbors = self.get_neighbors(current_vertex)
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], self.get_weight(current_vertex, neighbor) + weight))
                    visited.add(neighbor)

        return None
    
    @timer(msg="A*")
    def a_star(self, start_vertex, target_vertex):
        pass

    @timer(msg="Best First")
    def best_first(self, start_vertex, target_vertex):
        pass
