import heapq
import random
import time

def dijkstra(start, get_neighbors):
    distances = {start: 0}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in get_neighbors(current_node):
            distance = current_distance + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def get_random_neighbors(node):
    neighbors = []
    for j in range(int(node) + 1, NODES):
        weight = random.randint(1, 100)  # Random weight between 1 and 10
        neighbors.append((str(j), weight))
    return neighbors

# Create a provided number of nodes
NODES = 5

# Measure the time taken by the algorithm
start_time = time.time()

start_node = "0"  # We can directly use the string "0" as the start node

# Calculate the shortest distances from the start node
shortest_distances = dijkstra(start_node, get_random_neighbors)

print(shortest_distances)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")
