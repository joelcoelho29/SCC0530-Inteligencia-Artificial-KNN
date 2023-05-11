import random
import math

def generate(n, k):
    vertex_list = _generate_vertices(n)
    edge_list = _generate_edges(vertex_list, k)

    return vertex_list, edge_list

def _generate_vertices(n):
    vertex_list = []
    for i in range(n):
        x = math.floor(random.uniform(0, n))
        y = math.floor(random.uniform(0, n))
        vertex_list.append((i, x, y)) # Cada vértice é representado por uma tupla com id, x e y
    return vertex_list

def _generate_edges(vertex_list, k):
    edge_list = []
    for i, (id1, x1, y1) in enumerate(vertex_list):
        distances = []
        for j, (id2, x2, y2) in enumerate(vertex_list):
            if i == j: # Não cria aresta consigo mesmo
                continue
            distance = math.floor(math.sqrt((x1 - x2)**2 + (y1 - y2)**2)) # Distância geométrica entre os vértices
            distances.append((id2, distance))
        distances.sort(key=lambda x: x[1]) # Ordena as distâncias pelo valor da distância
        for j in range(k):
            id2, distance = distances[j]
            edge_list.append((id1, id2, distance)) # Cria uma aresta com o vértice mais próximo
    return edge_list