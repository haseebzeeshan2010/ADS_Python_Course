import heapq
import random
import time

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Create an empty graph
graph = {}

# Create a provided number of nodes
NODES = 5000


start_time = time.time()

# Add nodes to the graph
for i in range(NODES):
    node = str(i)
    graph[node] = {}

# Add random edges between the nodes
for i in range(NODES):
    for j in range(i+1, NODES):
        node1 = str(i)
        node2 = str(j)
        weight = random.randint(1, 10)  # Random weight between 1 and 10
        graph[node1][node2] = weight
        graph[node2][node1] = weight

print("Generated Graph")

start_node = "0"  # We can directly use the string "0" as the start node

# Measure the time taken by the algorithm


# Calculate the shortest distances from the start node
shortest_distances = dijkstra(graph, start_node)

print(shortest_distances)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")