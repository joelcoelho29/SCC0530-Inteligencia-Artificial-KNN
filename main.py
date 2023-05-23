import math
import random
import time
from knn.generate_knn import generate
from knn.plot_knn import plot
from graph import Graph
from view.tabulate import get_metrics

DISTINCT_PAIRS_TEST_AMOUNT = 10

def create_graph(knn_vertex_list, knn_edge_list):

    graph = Graph()

    # Função responsável por adicionar vértices no grafo
    for vertex in knn_vertex_list:
        graph.add_vertex(vertex)

    # Função responsável por adicionar as arestas no grafo
    for edge in knn_edge_list:
        graph.add_edge(edge[0], edge[1], edge[2])

    return graph


def create_random_vertices():
    vertices_pairs = []

    while len(vertices_pairs) < DISTINCT_PAIRS_TEST_AMOUNT:
        source = math.floor(random.uniform(0, n))
        target = math.floor(random.uniform(0, n))

        if source != target:
            vertices_pairs.append((source, target))

    return vertices_pairs


def execute_search_method(method, source, target):
    start = time.time()
    search_result = method(source, target)
    end = time.time()
    runtime = round(end - start, 3)
    if (search_result == None or search_result[0] == None or search_result[1] == None or search_result[2] == None):
        graph.print_path(None)
        return (0, runtime, 0)

    graph.print_path(search_result[0])
    return (search_result[1], runtime, search_result[2])

def execute(vertices_pairs):
    bfs_metrics = {"weights": [], "times": [], "visiteds": []}
    dfs_metrics = {"weights": [], "times": [], "visiteds": []}
    bf_metrics = {"weights": [], "times": [], "visiteds": []}
    astar_metrics = {"weights": [], "times": [], "visiteds": []}
    dijkstra_metrics = {"weights": [], "times": [], "visiteds": []}

    for i, (source, target) in enumerate(vertices_pairs):
        print(f"Busca {i+1}")
        print(f"Vertice de Origem: {source}")
        print(f"Vertice de Destino: {target}\n")

        weight, time, visiteds = execute_search_method(
            graph.breadth_first_search, source, target)
        bfs_metrics["weights"].append(weight)
        bfs_metrics["times"].append(time)
        bfs_metrics["visiteds"].append(visiteds)

        weight, time, visiteds = execute_search_method(
            graph.depth_first_search, source, target)
        dfs_metrics["weights"].append(weight)
        dfs_metrics["times"].append(time)
        dfs_metrics["visiteds"].append(visiteds)

        weight, time, visiteds = execute_search_method(
            graph.best_first, source, target)
        bf_metrics["weights"].append(weight)
        bf_metrics["times"].append(time)
        bf_metrics["visiteds"].append(visiteds)

        weight, time, visiteds = execute_search_method(
            graph.a_star, source, target)
        astar_metrics["weights"].append(weight)
        astar_metrics["times"].append(time)
        astar_metrics["visiteds"].append(visiteds)

        weight, time, visiteds = execute_search_method(
            graph.dijkstra, source, target)
        dijkstra_metrics["weights"].append(weight)
        dijkstra_metrics["times"].append(time)
        dijkstra_metrics["visiteds"].append(visiteds)

        print("X----------------------------------------------------------X\n")

    get_metrics(bfs_metrics, dfs_metrics, bf_metrics, astar_metrics, dijkstra_metrics, DISTINCT_PAIRS_TEST_AMOUNT)


# Definição do número total de vértices e da quantidade de conexõs entre os mesmos
n = 2000
k = 3

# Função responsável por gerar uma lista de vértices e uma lista de arestas de forma randômica
knn_vertex_list, knn_edge_list = generate(n, k)

# Criando o grafo
graph = create_graph(knn_vertex_list, knn_edge_list)

# Criando um conjunto de vértices de forma randômica
vertices_pairs = create_random_vertices()

# Executa todos os algoritmos de busca com os pares de vértices criados, exibindo métricas

execute(vertices_pairs)

# Plotando o gráfico
plot(knn_vertex_list, knn_edge_list)
