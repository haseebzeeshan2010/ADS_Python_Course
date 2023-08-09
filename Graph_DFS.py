def dfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    stack = [start]  # Stack to store nodes to visit

    while stack:
        node = stack.pop()  # Get the next node from the stack

        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node)  # Print or process the node as desired

            # Add the unvisited neighbors of the current node to the stack
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')