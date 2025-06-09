from dijkstra_algorithm import dijkstra
from visualize_graph import draw_graph

graph = {
    'DEL': {'BOM': 1200, 'BLR': 1700},
    'BOM': {'DEL': 1200, 'BLR': 980},
    'BLR': {'DEL': 1700, 'BOM': 980}
}

draw_graph(graph)
shortest_paths = dijkstra(graph, 'DEL')
print("Shortest paths from DEL:", shortest_paths)