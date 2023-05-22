import random
import math
from scipy.spatial import KDTree

from decorators.timer import timer

def generate(n, k):
    vertex_list = _generate_vertices(n)
    edge_list = _generate_edges(vertex_list, k)

    return vertex_list, edge_list


def _generate_vertices(n):
    vertex_list = []
    coordinates_set = set()
    
    for i in range(n):
        x = math.floor(random.uniform(0, n))
        y = math.floor(random.uniform(0, n))
        
        while (x, y) in coordinates_set:
            x = math.floor(random.uniform(0, n))
            y = math.floor(random.uniform(0, n))
        
        coordinates_set.add((x, y))
        vertex_list.append((i, x, y))
        
    return vertex_list

@timer(msg="_generate_edges")
def _generate_edges(vertex_list, k):
    edge_list = []
    # Cria a lista de coordenadas para a kd-tree
    coordinates = [(x, y) for _, x, y in vertex_list]
    
    # Cria a kd-tree
    kd_tree = KDTree(coordinates)
    
    for i, (id1, x1, y1) in enumerate(vertex_list):
        # Realiza a busca na kd-tree pelo k+1 vizinhos mais próximos (incluindo o próprio vértice)
        distances, indices = kd_tree.query([(x1, y1)], k=k+1)
        
        for j in indices[0][1:]:
            id2, x2, y2 = vertex_list[j]
            distance = math.floor(math.sqrt((x1 - x2)**2 + (y1 - y2)**2)) # Distância geométrica entre os vértices
            edge_list.append((id1, id2, distance)) # Cria uma aresta com o vértice mais próximo
    
    return edge_list