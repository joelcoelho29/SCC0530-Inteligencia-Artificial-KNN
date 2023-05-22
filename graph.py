import math
from decorators.timer import timer
from queue import PriorityQueue
from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.vertex = {}

    # Função auxiliar responsável por adicionar um vértice no gráfico
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            vertex_id = vertex[0]
            self.vertex[vertex_id] = (vertex[1], vertex[2])
            self.graph[vertex_id] = {}

    # Função auxiliar responsável por adicionar uma aresta no gráfico
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight

    # Função auxiliar reponsável por obter uma lista que contém todos os vértices vizinhos do vértice parametrizado
    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return list(self.graph[vertex].keys())
        else:
            return []

    # Função auxiliar reponsável por calcular e retornar o peso entre dois vértices
    def get_weight(self, source, target):
        if source in self.graph and target in self.graph[source]:
            if (source == target):
                return 0
            return self.graph[source][target]
        else:
            return None

    # Função responsável por executar o algoritmo Depth First Search
    @timer(msg="(DFS) Depth First Search")
    def depth_first_search(self, start_vertex, target_vertex):
        visited = set()
        stack = [(start_vertex, [start_vertex], 0)]

        while stack:
            current_vertex, path, weight = stack.pop()

            if current_vertex == target_vertex:
                return (path, weight, len(visited))

            visited.add(current_vertex)
            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(
                        (neighbor, path + [neighbor], self.get_weight(current_vertex, neighbor) + weight))

        return None

    # Função responsável por executar o algoritmo Breadth First Search
    @timer(msg="(BFS) Breadth First Search")
    def breadth_first_search(self, start_vertex, target_vertex):
        visited = set()
        queue = deque()

        queue.append((start_vertex, [start_vertex], 0))
        visited.add(start_vertex)

        while queue:
            current_vertex, path, weight = queue.popleft()

            if current_vertex == target_vertex:
                return (path, weight, len(visited))

            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(
                        (neighbor, path + [neighbor], self.get_weight(current_vertex, neighbor) + weight))
                    visited.add(neighbor)

        return None

    # Função responsável por executar o algoritmo A*
    @timer(msg="(A*) A*")
    def a_star(self, start_vertex, target_vertex):
        return self.actual_best_first(start_vertex, target_vertex, True)

    # Função responsável por executar o algoritmo Best First Search
    @timer(msg="(BF) Best First")
    def best_first(self, start_vertex, target_vertex):
        return self.actual_best_first(start_vertex, target_vertex, False)

    def actual_best_first(self, start_vertex, target_vertex, is_euclidian_heuristic):
        visited = set()
        current_path = [start_vertex]
        frontier = PriorityQueue()
        frontier.put((0, current_path, 0))

        while not frontier.empty():
            _, current_path, weight = frontier.get()
            current_vertex = current_path[-1]

            visited.add(current_vertex)

            if current_vertex == target_vertex:
                return (current_path, weight, len(visited))

            neighbors = self.get_neighbors(current_vertex)

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = current_path + [neighbor]
                    new_cost = self.get_weight(current_vertex, neighbor)

                    if (neighbor == target_vertex):
                        return (new_path, weight + new_cost, len(visited))
                    
                    heuristic = self.heuristic(
                        current_vertex, neighbor, target_vertex, is_euclidian_heuristic)
                    frontier.put((heuristic, new_path, weight + new_cost))

        return None

    @timer(msg="Dijkstra")
    def dijkstra(self, start_vertex, target_vertex):
        distances = {vertex: float('inf') for vertex in self.graph}
        previous = {vertex: None for vertex in self.graph}
        visited_nodes = 0  # Variável para contar o número de nós visitados
        
        distances[start_vertex] = 0
        
        pq = [(0, start_vertex)]
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            if current_distance > distances[current_vertex]:
                continue
            
            visited_nodes += 1
            
            if current_vertex == target_vertex:
                break
            
            for neighbor in self.get_neighbors(current_vertex):
                new_distance = distances[current_vertex] + self.get_weight(current_vertex, neighbor)
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_distance, neighbor))
        
        path = self._reconstruct_path(start_vertex, target_vertex, previous)
        
        total_weight = distances[target_vertex]
        
        return path, total_weight, visited_nodes

    # Função auxiliar para reconstruir o caminho percorrido
    def _reconstruct_path(self, start_vertex, target_vertex, previous):
        path = []
        current_vertex = target_vertex
        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]
        path.reverse()
        return path

    # Função auxiliar responsável determinar a heurística no método A*
    # OBS: Vale ressaltar que essa função é utilizada tanto pelo BF quanto pelo A*, o que difere é um boolean (is_euclidian_heuristic) que determina qual será a heurística que deve ser utilizada
    def heuristic(self, source, neighbor, target, is_euclidian_heuristic):
        if is_euclidian_heuristic:
            x1, y1 = self.vertex[neighbor]
            x2, y2 = self.vertex[target]

            return math.floor(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

        return self.get_weight(source, neighbor)

    # Função auxiliar responsável por dispor no terminal o caminho retornado pelos algoritmos de busca
    def print_path(self, path):
        if (path == None):
            print(f"Path not found :(")
            return

        print(f"Path: ", end='')

        for vertex in path:
            if (path.index(vertex) == len(path) - 1):
                print(f"{vertex}\n")
            else:
                print(f"{vertex} -> ", end='')
