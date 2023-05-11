import networkx as nx

import decorators.timer as dtimer

@dtimer.timer(msg="Depth First Search")
def search(graph, source, target):
    dfs_edges = nx.dfs_edges(graph, source)

    path_edges = [edge for edge in dfs_edges if edge[1] == target]

    path = [source]
    for edge in path_edges:
        path.append(edge[1])

    print(f"Caminho da busca em profundidade de {source} a {target}:")
    for node in path:
        print(node)

    return path