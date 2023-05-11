import search_algorithms.depth_search as depth
import search_algorithms.a_star_search as astar
import search_algorithms.best_first_search as bestfirst
import search_algorithms.breadth_first_search as breadhfirst
import knn.knn_nx
import knn.generate_knn
import knn.plot_knn

n = 50
k = 5

knn_vertex_list, knn_edge_list = knn.generate_knn.generate(n, k)

G = knn.knn_nx.convert(knn_vertex_list, knn_edge_list)

#knn.plot_knn.plot(G)
#knn.plot_knn.plot(knn_vertex_list, knn_edge_list)

source = 1
target = 49

depth.search(G, source, target)
astar.search(G, source, target)
bestfirst.search(G, source, target)
breadhfirst.search(G, source, target)
