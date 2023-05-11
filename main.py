import search_algorithms.depth_search as depth
import search_algorithms.a_star_search as astar
import search_algorithms.best_first_search as bestfirst
import search_algorithms.breadth_first_search as breadhfirst

import knn.generate_knn as knn
import knn.plot_knn as plotknn

knn_vertex_list, knn_edge_list = knn.generate(50, 3)

#plotknn.plot(knn_vertex_list, knn_edge_list)

depth.search()
astar.search()
bestfirst.search()
breadhfirst.search()
