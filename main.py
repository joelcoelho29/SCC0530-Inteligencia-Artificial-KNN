from knn.generate_knn import generate
from knn.plot_knn import plot

from graph import Graph

n = 20
k = 2

knn_vertex_list, knn_edge_list = generate(n, k)

g = Graph()

for vertex in knn_vertex_list:
   g.add_vertex(vertex[0])

for edge in knn_edge_list:
    g.add_edge(edge[0], edge[1], edge[2])

source = 1
target = 9

print(g.bfs(source, target))
print(g.dfs(source, target))
print(g.a_star(source, target))
print(g.best_first(source, target))

plot(knn_vertex_list, knn_edge_list)