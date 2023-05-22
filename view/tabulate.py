from tabulate import tabulate

def get_metrics(bfs_metrics, dfs_metrics, bf_metrics, astar_metrics, dijkstra_metrics, distinct_pairs_amount):
    print("Metricas: \n")
    table_weight = [["Buscas", "BFS Weight", "DFS Weight",
                     "BF Weight", "A* Weight", "Dijkstra"]]
    table_time = [["Buscas", "BFS Time", "DFS Time",
                   "BF Time", "A* Time", "Dijkstra"]]
    table_visiteds = [["Buscas", "BFS Visiteds",
                       "DFS Visiteds", "BF Visiteds", "A* Visiteds", "Dijkstra"]]

    for i in range(distinct_pairs_amount):
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

    avg_weight_line = ["Media total de peso", bfs_total_weight / distinct_pairs_amount, dfs_total_weight /
                       distinct_pairs_amount,  bf_total_weight / distinct_pairs_amount, astar_total_weight / distinct_pairs_amount, dijkstra_total_weight / distinct_pairs_amount]

    results_time_line = ["Total", bfs_total_time,
                         dfs_total_time, bf_total_time, astar_total_time, dijkstra_total_time]

    avg_time_line = ["Media total de tempo", bfs_total_time / distinct_pairs_amount, dfs_total_time /
                     distinct_pairs_amount, bf_total_time / distinct_pairs_amount, astar_total_time / distinct_pairs_amount, dijkstra_total_time / distinct_pairs_amount]

    results_visiteds_line = ["Total", bfs_total_visiteds,
                             dfs_total_visiteds, bf_total_visiteds, astar_total_visiteds, dijkstra_total_visiteds]

    avg_visiteds_line = ["Media total de vertices visitados", bfs_total_visiteds / distinct_pairs_amount, dfs_total_visiteds /
                         distinct_pairs_amount, bf_total_visiteds / distinct_pairs_amount, astar_total_visiteds / distinct_pairs_amount, dijkstra_total_visiteds / distinct_pairs_amount]

    table_weight.append(results_weight_line)
    table_weight.append(avg_weight_line)

    table_time.append(results_time_line)
    table_time.append(avg_time_line)

    table_visiteds.append(results_visiteds_line)
    table_visiteds.append(avg_visiteds_line)

    print(tabulate(table_weight, headers="firstrow"), "\n")
    print(tabulate(table_time, headers="firstrow"), "\n")
    print(tabulate(table_visiteds, headers="firstrow"))
