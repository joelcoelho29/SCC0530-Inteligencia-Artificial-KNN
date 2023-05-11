import networkx as nx
import matplotlib.pyplot as plt

def plot(knn_vertex_list, knn_edge_list):
    G = nx.Graph()

    for v in knn_vertex_list:
        G.add_node(v[0], pos=(v[1], v[2]))

    for a in knn_edge_list:
        G.add_edge(a[0], a[1], weight=a[2])

    pos = nx.get_node_attributes(G, 'pos')

    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): "{:.2f}".format(d['weight']) for u, v, d in G.edges(data=True)})
    plt.show()
