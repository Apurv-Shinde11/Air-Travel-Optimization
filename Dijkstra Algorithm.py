import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# ✈️ Graph of 9 cities with direct flight distances (in km)
graph = {
    'DEL': {'BOM': 1140, 'CCU': 1300, 'AMD': 950, 'BLR': 2150, 'GAU': 1700},
    'BOM': {'DEL': 1140, 'GOA': 580, 'HYD': 710, 'AMD': 520},
    'BLR': {'DEL': 2150, 'HYD': 570, 'CHN': 350, 'GOA': 600},
    'HYD': {'BOM': 710, 'BLR': 570, 'CHN': 630},
    'CHN': {'BLR': 350, 'HYD': 630, 'CCU': 1370},
    'CCU': {'DEL': 1300, 'CHN': 1370, 'GAU': 1000},
    'AMD': {'DEL': 950, 'BOM': 520},
    'GOA': {'BOM': 580, 'BLR': 600},
    'GAU': {'DEL': 1700, 'CCU': 1000}
}

# Run algorithm from source city
source = 'DEL'
shortest_paths = dijkstra(graph, source)

# Display results
print(f"\nShortest distances from {source}:\n")
for city, distance in shortest_paths.items():
    print(f"To {city} : {distance} km")