import heapq
import time

def max_value_for_min_weight(graph, source, destination):
    weight_queue = [(0, source)]
    value_queue = [(-float('inf'), source)]

    min_weight = {node: float('inf') for node in graph}
    max_value = {node: -float('inf') for node in graph}
    
    min_weight[source] = 0
    max_value[source] = 0
    
    while weight_queue:
        weight, node = heapq.heappop(weight_queue)
        _, max_value_node = heapq.heappop(value_queue)
        
        if node == destination:
            return max_value[destination]
        
        if weight > min_weight[node]:
            continue
        
        for neighbor, (edge_weight, edge_value) in graph[node].items():
            new_weight = weight + edge_weight
            new_value = max(max_value[node], edge_value)
            
            if new_weight < min_weight[neighbor]:
                min_weight[neighbor] = new_weight
                max_value[neighbor] = new_value
                heapq.heappush(weight_queue, (new_weight, neighbor))
                heapq.heappush(value_queue, (-new_value, neighbor))

# Example graph and nodes
graph = {
    'A': {'B': (2, 5), 'C': (3, 8)},
    'B': {'C': (1, 3), 'D': (4, 2)},
    'C': {'D': (2, 4)},
    'D': {}
}
source_node = 'A'
destination_node = 'D'

start_time = time.time()
result = max_value_for_min_weight(graph, source_node, destination_node)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Max Value for Min Weight: {result}")
print(f"Time taken: {elapsed_time:.6f} seconds")
