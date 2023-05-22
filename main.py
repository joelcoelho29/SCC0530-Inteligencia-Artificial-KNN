import math
import random
import time
from knn.generate_knn import generate
from knn.plot_knn import plot
from tabulate import tabulate
from graph import Graph

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
    if (search_result == None):
        graph.print_path(None)
        return (0, runtime)

    graph.print_path(search_result[0])
    return (search_result[1], runtime, search_result[2])


def get_metrics(bfs_metrics, dfs_metrics, bf_metrics, astar_metrics, dijkstra_metrics):
    print("Metricas: \n")
    table_weight = [["Buscas", "BFS Weight", "DFS Weight",
                     "BF Weight", "A* Weight", "Dijkstra"]]
    table_time = [["Buscas", "BFS Time", "DFS Time",
                   "BF Time", "A* Time", "Dijkstra"]]
    table_visiteds = [["Buscas", "BFS Visiteds",
                       "DFS Visiteds", "BF Visiteds", "A* Visiteds", "Dijkstra"]]

    for i in range(DISTINCT_PAIRS_TEST_AMOUNT):
        weight_line = [f"Busca {i+1}", bfs_metrics["weights"][i], dfs_metrics["weights"]
                       [i], bf_metrics["weights"][i], astar_metrics["weights"][i], dijkstra_metrics["weights"][i]]
        time_line = [f"Busca {i+1}", bfs_metrics["times"][i], dfs_metrics["times"]
                     [i], bf_metrics["times"][i], astar_metrics["times"][i], dijkstra_metrics["times"][i]]
        visited_line = [f"Busca {i+1}", bfs_metrics["visiteds"][i], dfs_metrics["visiteds"]
                        [i], bf_metrics["visiteds"][i], astar_metrics["visiteds"][i], dijkstra_metrics["visiteds"][i]]
        table_weight.append(weight_line)
        table_time.append(time_line)
        table_visiteds.append(visited_line)

    bfs_total_weight = sum(bfs_metrics["weights"])
    dfs_total_weight = sum(dfs_metrics["weights"])
    bf_total_weight = sum(bf_metrics["weights"])
    astar_total_weight = sum(astar_metrics["weights"])
    dijkstra_total_weight = sum(dijkstra_metrics["weights"])

    bfs_total_time = sum(bfs_metrics["times"])
    dfs_total_time = sum(dfs_metrics["times"])
    bf_total_time = sum(bf_metrics["times"])
    astar_total_time = sum(astar_metrics["times"])
    dijkstra_total_time = sum(dijkstra_metrics["times"])

    bfs_total_visiteds = sum(bfs_metrics["visiteds"])
    dfs_total_visiteds = sum(dfs_metrics["visiteds"])
    bf_total_visiteds = sum(bf_metrics["visiteds"])
    astar_total_visiteds = sum(astar_metrics["visiteds"])
    dijkstra_total_visiteds = sum(dijkstra_metrics["visiteds"])

    results_weight_line = ["Total", bfs_total_weight,
                           dfs_total_weight, bf_total_weight, astar_total_weight, dijkstra_total_weight]

    avg_weight_line = ["Media total de peso", bfs_total_weight / DISTINCT_PAIRS_TEST_AMOUNT, dfs_total_weight /
                       DISTINCT_PAIRS_TEST_AMOUNT,  bf_total_weight / DISTINCT_PAIRS_TEST_AMOUNT, astar_total_weight / DISTINCT_PAIRS_TEST_AMOUNT, dijkstra_total_weight / DISTINCT_PAIRS_TEST_AMOUNT]

    results_time_line = ["Total", bfs_total_time,
                         dfs_total_time, bf_total_time, astar_total_time, dijkstra_total_time]

    avg_time_line = ["Media total de tempo", bfs_total_time / DISTINCT_PAIRS_TEST_AMOUNT, dfs_total_time /
                     DISTINCT_PAIRS_TEST_AMOUNT, bf_total_time / DISTINCT_PAIRS_TEST_AMOUNT, astar_total_time / DISTINCT_PAIRS_TEST_AMOUNT, dijkstra_total_time / DISTINCT_PAIRS_TEST_AMOUNT]

    results_visiteds_line = ["Total", bfs_total_visiteds,
                             dfs_total_visiteds, bf_total_visiteds, astar_total_visiteds, dijkstra_total_visiteds]

    avg_visiteds_line = ["Media total de vertices visitados", bfs_total_visiteds / DISTINCT_PAIRS_TEST_AMOUNT, dfs_total_visiteds /
                         DISTINCT_PAIRS_TEST_AMOUNT, bf_total_visiteds / DISTINCT_PAIRS_TEST_AMOUNT, astar_total_visiteds / DISTINCT_PAIRS_TEST_AMOUNT, dijkstra_total_visiteds / DISTINCT_PAIRS_TEST_AMOUNT]

    table_weight.append(results_weight_line)
    table_weight.append(avg_weight_line)

    table_time.append(results_time_line)
    table_time.append(avg_time_line)

    table_visiteds.append(results_visiteds_line)
    table_visiteds.append(avg_visiteds_line)

    print(tabulate(table_weight, headers="firstrow"), "\n")
    print(tabulate(table_time, headers="firstrow"), "\n")
    print(tabulate(table_visiteds, headers="firstrow"))


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

    get_metrics(bfs_metrics, dfs_metrics, bf_metrics, astar_metrics, dijkstra_metrics)


# Definição do número total de vértices e da quantidade de conexõs entre os mesmos
n = 2000
k = 7

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
