import heapq
import random

def max_value_dijkstra(graph, start):
    distances = {node: float('-inf') for node in graph}
    distances[start] = float('inf')

    priority_queue = [(float('-inf'), start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        neg_distance, node = heapq.heappop(priority_queue)
        distance = -neg_distance

        if distance < distances[node]:
            continue

        for neighbor, weight in graph[node].items():
            new_distance = min(distance, weight)
            if new_distance > distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (-new_distance, neighbor))

    return distances

# Function to generate a random graph with a specified number of nodes and edges.
def generate_random_graph(num_nodes, num_edges):
    graph = {str(node): {} for node in range(num_nodes)}
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        weight = random.randint(1, 100)
        if u != v and v not in graph[str(u)]:
            graph[str(u)][str(v)] = weight
    return graph

num_nodes = 5
num_edges = 10000
start_node = '0'  # Start from node 0

# Generate random graph and calculate shortest distances using max_value_dijkstra.
graph = generate_random_graph(num_nodes, num_edges)
shortest_distances = max_value_dijkstra(graph, start_node)

print("Shortest distances from", start_node, "to all nodes:")
for node, distance in shortest_distances.items():
    print(node, ":", distance)
