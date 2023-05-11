import networkx as nx

def convert(knn_vertex_list, knn_edge_list):
    G = nx.Graph()

    for v in knn_vertex_list:
        G.add_node(v[0], pos=(v[1], v[2]))

    for a in knn_edge_list:
        G.add_edge(a[0], a[1], weight=a[2])

    return G