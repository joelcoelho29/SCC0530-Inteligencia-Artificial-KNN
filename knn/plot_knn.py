import networkx as nx
import matplotlib.pyplot as plt
import knn.knn_nx

# plot using converted knn to nx graph
def plot(G):
    pos = nx.get_node_attributes(G, 'pos')

    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): "{:.2f}".format(d['weight']) for u, v, d in G.edges(data=True)})
    plt.show()


# plot using knn_vertex_list, knn_edge_list
def plot(knn_vertex_list, knn_edge_list):
    G = knn.knn_nx.convert(knn_vertex_list, knn_edge_list)

    pos = nx.get_node_attributes(G, 'pos')

    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): "{:.2f}".format(d['weight']) for u, v, d in G.edges(data=True)})
    plt.show()