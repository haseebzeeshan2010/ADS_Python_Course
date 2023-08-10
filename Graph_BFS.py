class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

def bfs(graph, start):
    visited = set()
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")  # You can modify this line to store or process the visited nodes
            visited.add(node)
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                queue.append(neighbor)


# Create a graph
g = Graph()

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Call BFS
print("BFS Traversal:")
bfs(g.graph, 2)