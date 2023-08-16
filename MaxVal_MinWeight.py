import heapq

def max_value_for_min_weight(graph, start):
    # Initialize distances to all nodes as negative infinity
    distances = {node: float('-inf') for node in graph}
    # Set the distance of the start node to 0
    distances[start] = 0

    # Priority queue to store nodes and their associated distances
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if the current distance is less than the stored distance
        if current_distance < distances[current_node]:
            continue

        for neighbor, (weight, value) in graph[current_node].items():
            # Calculate the new combined value-weight ratio
            new_ratio = (distances[current_node] + value) / weight

            # If the new ratio is greater than the stored ratio, update the values
            if new_ratio > distances[neighbor]:
                distances[neighbor] = new_ratio
                heapq.heappush(pq, (new_ratio, neighbor))

    return distances

# Example graph represented as an adjacency dictionary
graph = {
    'A': {'B': (2, 5), 'C': (1, 10)},
    'B': {'C': (3, 2), 'D': (4, 8)},
    'C': {'D': (2, 4)},
    'D': {'E': (3, 6)},
    'E': {}
}

start_node = 'A'
shortest_distances = max_value_for_min_weight(graph, start_node)
print("Shortest distances from node", start_node)
for node, distance in shortest_distances.items():
    print(node, "-", distance)
